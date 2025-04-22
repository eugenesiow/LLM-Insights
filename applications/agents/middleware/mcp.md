# Model Context Protocol (MCP)

The Model Context Protocol (MCP) is what I'd describe as a middleware layer, a standardized integration layer, for agents. It is not itself an "agent framework". Rather, MCP provides agents with (standardized, secure and structured) plumbing to connect and perform actions involving external data or tools. 

## How to Talk to MCP Servers

Let's dive in with a practical example (we borrow heavily from the [dolphin-mcp](https://github.com/cognitivecomputations/dolphin-mcp/) implementation) on how a client communicates with an MCP server, keeping all communication local (same machine) for now. 

First, we start with a configuration file, `mcp_config.json`, that specifies a set of MCP servers. This configuration file specifies that we will start an sqlite MCP server called `mcp-server-sqlite` with a sqlite db called `./demo.db`.  We will use `uvx` (requires python and [`uv`](https://github.com/astral-sh/uv) to be installed) to install all the dependencies and start the server at runtime.

```json
{
  "mcpServers": {
    "demo-database-sqlite": {
      "command": "uvx",
      "args": [
        "mcp-server-sqlite",
        "--db-path",
        "./demo.db"
      ]
    } 
  }
}
```

Now lets write some code to read the configuration file and spin up the server and have a client connect to that server. Note that an individual client is required for each MCP server you want to connect to. We create an async function called `run_client` which reads in the config file and for each server in the `mcpServers` object within our config file, `mcp_config.json`, we'll create an `MCPClient` and `.start()` it (this starts both the server and client connecting to it).

```python
import json
import asyncio

async def run_client(config_path: str = "mcp_config.json", config: Optional[dict] = None):
    if config is None:    
        with open(config_path, "r") as f:
            config = json.load(f)
            servers_cfg = config.get("mcpServers", {})

    for server_name, conf in servers_cfg.items():
        client = MCPClient(
            server_name=server_name,
            command=conf.get("command"),
            args=conf.get("args", []),
            env=conf.get("env", {})
        )
        ok = await client.start()

if __name__ == "__main__":
    asyncio.run(run_client(
        config_path="mcp_config.json"
    ))
```

Within `MCPClient` we create the async function called `start()` where we create a subprocess that calls `uvx` to pull `mcp-server-sqlite` and run it. We also map the `stdio`, standard input output pipe, from the client to the server which is created in the subprocess.

```python
class MCPClient:
    async def start(self):       
        try:
            self.process = await asyncio.create_subprocess_exec(
                self.command,
                stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            self.receive_task = asyncio.create_task(self._receive_loop())
            return await self._perform_initialize()
        except Exception:
            return False
```

### Initialization

Notice that we call the `_perform_initialize()` internal function within our class. This is an initialization function between our new client and the server that we've spun up using `uvx`. It will first send an `initialize` message, and will receive a result from the server with metadata like `serverInfo`, `protocolVersion` and `capabilities`. After that the client will send out a notification `notifications/initialized` that the initialization process was succesfuly.

<details>
<summary>1. Initialize Request (From Client)</summary>

```json
{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "protocolVersion": "2024-11-05",
        "capabilities": {
            "sampling": {}
        },
        "clientInfo": {
            "name": "OurMCPClient",
            "version": "1.0.0"
        }
    }
}
```

</details>

<details>
<summary>2. Initialize Result (From Server)</summary>

```json
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "protocolVersion": "2024-11-05",
        "capabilities": {
            "experimental": {},
            "prompts": {
                "listChanged": false
            },
            "resources": {
                "subscribe": false,
                "listChanged": false
            },
            "tools": {
                "listChanged": false
            }
        },
        "serverInfo": {
            "name": "sqlite",
            "version": "0.1.0"
        }
    }
}
```

</details>

<details>
<summary>3. Notification Initialized (From Client)</summary>

```json
{
    "jsonrpc": "2.0",
    "method": "notifications/initialized"
}
```

</details>

This process of message exchange for the initialization is shown in code within the `_perform_initialize()` function below:

```python
async def _perform_initialize(self):
    self.request_id += 1
    req_id = self.request_id
    req = {
        "jsonrpc": "2.0",
        "id": req_id,
        "method": "initialize",
        "params": {
            "protocolVersion": self.protocol_version,
            "capabilities": {"sampling": {}},
            "clientInfo": {
                "name": "OurMCPClient",
                "version": "1.0.0"
            }
        }
    }
    await self._send_message(req)

    start = asyncio.get_event_loop().time()
    timeout = 10  # Increased timeout to 10 seconds
    while asyncio.get_event_loop().time() - start < timeout:
        if req_id in self.responses:
            resp = self.responses[req_id]
            del self.responses[req_id]
            if "error" in resp:
                logger.error(f"Server {self.server_name}: Initialize error: {resp['error']}")
                return False
            if "result" in resp:
                elapsed = asyncio.get_event_loop().time() - start
                logger.info(f"Server {self.server_name}: Initialized in {elapsed:.2f}s")
                note = {"jsonrpc": "2.0", "method": "notifications/initialized"}
                await self._send_message(note)
                init_result = resp["result"]
                self.server_capabilities = init_result.get("capabilities", {})
                return True
        await asyncio.sleep(0.05)
    logger.error(f"Server {self.server_name}: Initialize timed out after {timeout}s")
    return False
```

The `_send_message()` function is as follows. Since we are doing local communications, these messages use the `stdin` pipe between the client process and the server subprocess.

```python
async def _send_message(self, message: dict):
    if not self.process or self._shutdown:
        logger.error(f"Server {self.server_name}: Cannot send message - process not running or shutting down")
        return False
    try:
        data = json.dumps(message) + "\n"
        self.process.stdin.write(data.encode())
        await self.process.stdin.drain()
        return True
    except Exception as e:
        logger.error(f"Server {self.server_name}: Error sending message: {str(e)}")
        return False
```

Now let's back up abit and recall the `start()` function. We set the `receive_task` to be a `_receive_loop()` function. This is a function that will process messages from the server to the client. Below are the `_receive_loop()` and `_process_message()` functions. The receive loop reads lines from the `stdout`, each of it is a message which is then sent to the `_process_message()` function. If the messages are correctly formatted (JSON, has `jsonrpc`, `id`, `result`), the message are stored in an in memory dictionary within the client class indexed by the the message `id`.

```python
async def _receive_loop(self):
    if not self.process or self.process.stdout.at_eof():
        return
    try:
        while not self.process.stdout.at_eof():
            line = await self.process.stdout.readline()
            if not line:
                break
            try:
                message = json.loads(line.decode().strip())
                self._process_message(message)
            except json.JSONDecodeError:
                pass
    except Exception:
        pass

def _process_message(self, message: dict):
    if "jsonrpc" in message and "id" in message:
        if "result" in message or "error" in message:
            self.responses[message["id"]] = message
        else:
            # request from server, not implemented
            resp = {
                "jsonrpc": "2.0",
                "id": message["id"],
                "error": {
                    "code": -32601,
                    "message": f"Method {message.get('method')} not implemented in client"
                }
            }
            asyncio.create_task(self._send_message(resp))
    elif "jsonrpc" in message and "method" in message and "id" not in message:
        # notification from server
        pass
```

### Listing Tools

Next up we want to be able to find out what tools are available and how to call them from the client. We send a list tools request to the server and receive a result on each of the tools, their descriptions and input schema, including parameters. Again the list tools request is a simple JSON-RPC with a `tools/list` method. The result is a list of tools like `read_query` and `create_table`.

<details>
<summary>1. List Tools Request (From Client)</summary>

```json
{
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/list",
    "params": {}
}
```

</details>

<details>
<summary>2. List Tools Result (From Server)</summary>

```json
{
    "jsonrpc": "2.0",
    "id": 2,
    "result": {
        "tools": [
            {
                "name": "read_query",
                "description": "Execute a SELECT query on the SQLite database",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "SELECT SQL query to execute"
                        }
                    },
                    "required": [
                        "query"
                    ]
                }
            },
            {
                "name": "write_query",
                "description": "Execute an INSERT, UPDATE, or DELETE query on the SQLite database",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "SQL query to execute"
                        }
                    },
                    "required": [
                        "query"
                    ]
                }
            },
            {
                "name": "create_table",
                "description": "Create a new table in the SQLite database",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "CREATE TABLE SQL statement"
                        }
                    },
                    "required": [
                        "query"
                    ]
                }
            },
            {
                "name": "list_tables",
                "description": "List all tables in the SQLite database",
                "inputSchema": {
                    "type": "object",
                    "properties": {}
                }
            },
            {
                "name": "describe_table",
                "description": "Get the schema information for a specific table",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "table_name": {
                            "type": "string",
                            "description": "Name of the table to describe"
                        }
                    },
                    "required": [
                        "table_name"
                    ]
                }
            },
            {
                "name": "append_insight",
                "description": "Add a business insight to the memo",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "insight": {
                            "type": "string",
                            "description": "Business insight discovered from data analysis"
                        }
                    },
                    "required": [
                        "insight"
                    ]
                }
            }
        ]
    }
}
```

</details>

The following is the `list_tools()` code. As we've discussed above, it first sends a `tools/list` function to the server and then receives a result with a list of `tools` from the MCP server. The function returns this list of tools.

```python
async def list_tools(self):
    if not self.process:
        return []
    self.request_id += 1
    rid = self.request_id
    req = {
        "jsonrpc": "2.0",
        "id": rid,
        "method": "tools/list",
        "params": {}
    }
    await self._send_message(req)

    start = asyncio.get_event_loop().time()
    timeout = 10  # Increased timeout to 10 seconds
    while asyncio.get_event_loop().time() - start < timeout:
        if rid in self.responses:
            resp = self.responses[rid]
            del self.responses[rid]
            if "error" in resp:
                logger.error(f"Server {self.server_name}: List tools error: {resp['error']}")
                return []
            if "result" in resp and "tools" in resp["result"]:
                elapsed = asyncio.get_event_loop().time() - start
                logger.info(f"Server {self.server_name}: Listed {len(resp['result']['tools'])} tools in {elapsed:.2f}s")
                self.tools = resp["result"]["tools"]
                return self.tools
        await asyncio.sleep(0.05)
    logger.error(f"Server {self.server_name}: List tools timed out after {timeout}s")
    return []
```

### Calling Tools

The client can also call tools wrapped by the MCP server and return any outputs. To call a tool, we fire a request with a `tools/call` method. In the `params`, we need to specify the `name` of the tool and any `arguments` that should be passed to the tool. We are returned a response with the outputs.

<details>
<summary>1. Call Tool Request (From Client)</summary>

```json
{
    "jsonrpc": "2.0",
    "id": 3,
    "method": "tools/call",
    "params": {
        "name": "list_tables",
        "arguments": {}
    }
}
```

</details>

<details>
<summary>2. Call Tool Result (From Server)</summary>

```json
{
    "jsonrpc": "2.0",
    "id": 3,
    "result": {
        "content": [
            {
                "type": "text",
                "text": "[{'name': 'dolphin_species'}, {'name': 'evolutionary_relationships'}]"
            }
        ],
        "isError": false
    }
}
```

</details>

The following is the `call_tool()` code. As we've discussed above, it sends a `tools/call` function to the server to run the tool and the outputs are sent back as `content`.

```python
async def call_tool(self, tool_name: str, arguments: dict):
    if not self.process:
        return {"error": "Not started"}
    self.request_id += 1
    rid = self.request_id
    req = {
        "jsonrpc": "2.0",
        "id": rid,
        "method": "tools/call",
        "params": {
            "name": tool_name,
            "arguments": arguments
        }
    }
    await self._send_message(req)

    start = asyncio.get_event_loop().time()
    timeout = 3600  # Increased timeout to 30 seconds
    while asyncio.get_event_loop().time() - start < timeout:
        if rid in self.responses:
            resp = self.responses[rid]
            del self.responses[rid]
            if "error" in resp:
                logger.error(f"Server {self.server_name}: Tool {tool_name} error: {resp['error']}")
                return {"error": resp["error"]}
            if "result" in resp:
                elapsed = asyncio.get_event_loop().time() - start
                logger.info(f"Server {self.server_name}: Tool {tool_name} completed in {elapsed:.2f}s")
                return resp["result"]
        await asyncio.sleep(0.01)  # Reduced sleep interval for more responsive streaming
        if asyncio.get_event_loop().time() - start > 5:  # Log warning after 5 seconds
            logger.warning(f"Server {self.server_name}: Tool {tool_name} taking longer than 5s...")
    logger.error(f"Server {self.server_name}: Tool {tool_name} timed out after {timeout}s")
    return {"error": f"Timeout waiting for tool result after {timeout}s"}
```

### Client-to-LLM

For this example, we will get queries from the user, pass them to the LLM, process any tool calls, pass the outputs to the LLM and return the generations to the user. This follows the standard (OpenAI function calling API) flow of [function calling/tool use](function_calling.md).

Before we start the client-to-user loop, we first want to use `list_tools()` to setup a system prompt to pass to the LLM.

For example, the following system prompt, `SYSTEM_PROMPT` works well with `Llama-3.3-70B-Instruct` and `Qwen2.5-72B-Instruct-AWQ` and with vLLM and its tool-calling API (coherent with the chat completion API from OpenAI).

```markdown
You are a helpful assistant capable of accessing external functions and engaging in casual chat. Use the responses from these function calls to provide accurate and informative answers. The answers should be natural and hide the fact that you are using tools to access real-time information. Guide the user about available tools and their capabilities. Always utilize tools to access real-time information when required. Engage in a friendly manner to enhance the chat experience.

# Tools

{tools}

# Notes 

- Ensure responses are based on the latest information available from function calls.
- Maintain an engaging, supportive, and friendly tone throughout the dialogue.
- Always highlight the potential of available tools to assist users comprehensively.
```

For the `mcp-server-sqlite` server, the following tools are returned by `list_tools()` and populate the `{tools}` section of the system message.

```markdown
- read_query: Execute a SELECT query on the SQLite database
- write_query: Execute an INSERT, UPDATE, or DELETE query on the SQLite database
- create_table: Create a new table in the SQLite database
- describe_table: Get the schema information for a specific table
- append_insight: Add a business insight to the memo
```

The following schema is also passed in to the tools specification part of the chat completions API.

```json
[
    {
        "type": "function",
        "function": {
            "name": "read_query",
            "description": "Execute a SELECT query on the SQLite database",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "SELECT SQL query to execute"
                    }
                },
                "required": [
                    "query"
                ]
            }
        }
    },
    ...
]
```

So the above list is created and sent in the `tools` key within the `create()` function as shown below.

```python
first_response = await client.chat.completions.create(
    model=MODEL_ID,
    messages=messages,
    tools=([t["schema"] for t in tools.values()] if len(tools) > 0 else None),
    max_tokens=4096,
    temperature=0,
)
```

The messages passed in are the system prompt we defined earlier and the query we get from the user:

```python
messages.append({
    "role": "system",
    "content": SYSTEM_PROMPT.format(
        tools="\n- ".join(
            [
                f"{t['name']}: {t['schema']['function']['description']}"
                for t in tools.values()
            ]
        )
    ),  # Creates System prompt based on available MCP server tools
})    
messages.append({"role": "user", "content": query})
```

We can then check if the `finish_reason` from the response, `first_response.choices[0].finish_reason`, is `tool_calls` or `stop`. If it's `tool_calls` we can iterate through `first_response.choices[0].message.tool_calls` as follows, make the actual tool calls with the specified arguments and then add the results to a new chat completion request:

```python
for tool_call in first_response.choices[0].message.tool_calls:
    arguments = (
        json.loads(tool_call.function.arguments)
        if isinstance(tool_call.function.arguments, str)
        else tool_call.function.arguments
    )

    # Call the tool with the arguments using our callable initialized in the tools dict
    tool_result = await tools[tool_call.function.name]["callable"](**arguments)

    # Add the tool result to the messages list
    messages.append(
        {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "name": tool_call.function.name,
            "content": json.dumps(tool_result),
        }
    )

# Query LLM with the user query and the tool results
new_response = await client.chat.completions.create(
    model=MODEL_ID,
    messages=messages,
)
```

Let's say we submit the query `list tables` for example, the generated tool call `tool_call.function.name` is `read_query` and the arguments are in the JSON format (`tool_call.function.arguments`) as follows:

```json
{"query": "SELECT name FROM sqlite_master WHERE type=\'table\';"}
```

Calling the function using `await tools[tool_call.function.name]["callable"](**arguments)` gives us the `tool_result` of the two tables in the database:

```json
[{"name": "dolphin_species"}, {"name": "evolutionary_relationships"}]
```

From there we appended this as a JSON object to the `messages` object and sent it to the LLM for `new_response`, which gets back a `ChatCompletionMessage` with the content as follows (the `finish_reason` is now `stop`):

```markdown
Sure! Here are the tables in the database:

1. **dolphin_species**
2. **evolutionary_relationships**

Would you like to know more about any specific table? For example, I can describe the schema or fetch some data from it.
```

This content can then be used to continue the conversation.

## Ecosystem

- [FastAPI-MCP](https://github.com/tadata-org/fastapi_mcp) - automatically expose FastAPI endpoints as Model Context Protocol (MCP) servers with this library.
- [mcp-proxy](https://github.com/sparfenyuk/mcp-proxy) - connect to MCP servers that run on SSE transport, or expose stdio servers as an SSE server.
- [mcp-use](https://github.com/mcp-use/mcp-use) - quickstart library for glueing together an MCP capable agent.

### Catalogues

- [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) - (big) catalogue of MCP servers.