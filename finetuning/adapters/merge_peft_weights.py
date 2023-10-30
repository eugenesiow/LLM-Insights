import torch
from peft import PeftModel
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig


BASE_MODEL = "../BASE_MODEL"
LORA_WEIGHTS = "./ADAPTER_WEIGHTS"
MERGED_MODEL = "./MERGED_MODEL"

tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)

nf4_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
    bnb_4bit_compute_dtype=torch.bfloat16
)
model = AutoModelForCausalLM.from_pretrained(BASE_MODEL,
                                            load_in_8bit=False,
                                            torch_dtype=torch.bfloat16,
                                            device_map="auto")
model = PeftModel.from_pretrained(model, LORA_WEIGHTS)

model = model.merge_and_unload()
model.save_pretrained(MERGED_MODEL)
