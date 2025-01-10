from lxml.html.diff import token
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import transformers
from transformers import pipeline
from agents.scraping.scrapingTool2 import wiki_search as ws
import os

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.3-70B-Instruct")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.3-70B-Instruct")



def fact_model(data, keyword):
    model_id = "meta-llama/Llama-3.3-70B-Instruct"
    pipe = transformers.pipeline(
        "text-generation",
        model=model_id,
        torch_dtype=torch.bfloat16,
        device_map="auto",
    )

    messages = [
        {"role": "system",
         "content": f"You are a fact checking chatbot. The user will provide you with a large text. You will fact check it and make any modifications to the text that are necessary. Your response should be sound and scientific correct."},
        {"role": "user", "content": f"{data}"},
    ]

    inputs = tokenizer.apply_chat_template(messages, tools=ws(keyword), add_generation_prompt=True)


    tool_call = {"name": "wiki_search", "arguments": {"keyword": keyword}}
    messages.append({"role": "tool", "name": "ws", "call": tool_call})



    outputs = pipe(
        messages,
        max_new_tokens=5000,
    )
    print(outputs[0]["generated_text"][-1])
    return outputs[0]["generated_text"][-1]["content"]

