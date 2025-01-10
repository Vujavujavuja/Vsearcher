from idlelib.iomenu import encoding

import torch
from transformers import pipeline
import os

def get_data():
    path_to_data = "C:\\Users\\nvuji\OneDrive\Documents\GitHub\deepLearning2\\agents\scraping\output_data"
    data = ""
    for file in os.listdir(path_to_data):
        with open(os.path.join(path_to_data, file), "r", encoding="utf-8") as f:
            data += f.read()
    return data

def model(keyword, data):
    model_id = "meta-llama/Llama-3.2-1B-Instruct"
    pipe = pipeline(
        "text-generation",
        model=model_id,
        torch_dtype=torch.bfloat16,
        device_map="auto",
    )

    messages = [
        {"role": "system", "content": f"You are a summarization chatbot. The user will provide you with a large text consisting of 6 combined txt documents. You will summarize it into a single large text. Your response should be well structured and detailed. For the main keyword: {keyword}"},
        {"role": "user", "content": f"{data}"},
    ]
    outputs = pipe(
        messages,
        max_new_tokens=5000,
    )
    print(outputs[0]["generated_text"][-1])
    return outputs[0]["generated_text"][-1]["content"]

if __name__ == '__main__':
    model("Enigma", get_data())