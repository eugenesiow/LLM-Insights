# Nexus Function Calling Benchmark

The Nexus Function Calling Benchmark, or Nexus for short, is a functional calling/tool use benchmark with 9 tasks covering a spectrum, from cybersecurity and climate APIs to recommendation systems, along with some pure Python functions. The benchamrk is executed in a zero-shot way, meaning that models are tested on their innate ability to handle tasks they may not have been trained specifically for, showcasing their versatility and comprehension from the function definitions and user queries only. It is developed by the Nexusflow.ai team.

## Links

* Blog: https://nexusflow.ai/blogs/ravenv2
* Leaderboard: https://huggingface.co/spaces/Nexusflow/Nexus_Function_Calling_Leaderboard
* Code: (Notebooks) https://github.com/nexusflowai/NexusRaven-V2/blob/master/evaluation_notebook
* License: [Apache 2.0](https://github.com/nexusflowai/NexusRaven-V2?tab=readme-ov-file#license) (The repository states "The code in this repository for running the NexusRaven-V2 model, the evaluation notebook, the prompting notebook, and the evaluation data are licensed under Apache 2.0."), [CC-BY-NC-SA-4.0](https://huggingface.co/datasets/Nexusflow/Function_Call_Definitions/blob/main/README.md) (Function Call Definitions Dataset)

## Tasks

8 of the tasks have been released while the ninth task (The Stack API) is withheld. 

| #  | API                                                                                          | Category                  |
|----|-----------------------------------------------------------------------------------------------|---------------------------|
| 1  | [OTX](https://huggingface.co/datasets/Nexusflow/OTXAPIBenchmark)                             | Single Calls              |
| 2  | [NVDLibrary](https://huggingface.co/datasets/Nexusflow/NVDLibraryBenchmark)                  | Single Calls              |
| 3  | [VirusTotal](https://huggingface.co/datasets/Nexusflow/VirusTotalBenchmark)                  | Single Calls              |
| 4  | [VirusTotal-Nested Calls](https://huggingface.co/datasets/Nexusflow/VirusTotalMultiple)      | Nested Calls              |
| 5  | [Climate](https://huggingface.co/datasets/Nexusflow/ClimateAPIBenchmark)                     | Nested and Parallel Calls |
| 6  | [VirusTotal-Parallel Calls](https://huggingface.co/datasets/Nexusflow/VirusTotalMultiple)    | Parallel Calls            |
| 7  | [Places API](https://huggingface.co/datasets/Nexusflow/PlacesAPIBenchmark)                   | Nested Calls              |
| 8  | [NVDLibrary-Nested Calls](https://huggingface.co/datasets/Nexusflow/CVECPEAPIBenchmark)      | Nested Calls              |
| 9  | The Stack API                                                                                 | Mostly Single Calls       |

The [function definitions for all benchmarks](https://huggingface.co/datasets/Nexusflow/Function_Call_Definitions) are available. Single Calls are defined as API usage that only require a single function call. Nested Calls are defined as API usage that require multiple calls all at once to get the right answer, where the argument for the outer call depends on the call graph. Finally, parallel calls are when seperate calls are generated, but they do not connect into each other.

## Example Questions

<details>
<summary>OTX Sample - Single Call</summary>

**Prompt:**

> Using AlienVault, I need to check for any malware connections to 'techupdate.io'. My API key is 'UpdateKey456'.        

**API Use:**

```python
getIndicatorForHostname(apiKey="UpdateKey456", hostname="techupdate.io", section="malware")
```

</details>

<details>
<summary>Climate Sample - Nested Call</summary>

**Prompt:**

> What has been the weather like for the past 7 days?

**API Use:**

```python
get_hourly_observation(
    get_nearest_station_id(
        find_nearby_stations(get_latitude_longitude(get_current_location()))
    ),
    subtract_time_delta(
        get_current_time_at_location(get_latitude_longitude(get_current_location())), 7
    ),
    get_current_time_at_location(get_latitude_longitude(get_current_location())),
    get_timezone(get_latitude_longitude(get_current_location()))
)
```

</details>

<details>
<summary>Places API Sample - Parallel Call</summary>

**Prompt:**

> What are people saying about Ramen Nagi, So Gong, and McDonalds and how would you compare them? Also, after that, get me the distance from Ramen Nagi and So Gong?

**API Use:**

```python
get_some_reviews(["Ramen Nagi", "So Gong", "McDonalds"])
get_distance("Ramen Nagi", "So Gong")
```

</details>

## Citations

```bibtex
@misc{nexusraven,
      title={NexusRaven-V2: Surpassing GPT-4 for Zero-shot Function Calling},
      author={Nexusflow.ai team},
      year={2023},
      url={https://nexusflow.ai/blogs/ravenv2}
}
```