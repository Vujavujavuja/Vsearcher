# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained(
    "meta-llama/Llama-3.2-1B",
    token=HUGGING_FACE_TOKEN
)
model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-3.2-1B",
    token=HUGGING_FACE_TOKEN
)