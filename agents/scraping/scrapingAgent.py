from idlelib.iomenu import encoding

import torch
from transformers import pipeline, AutoModelForCausalLM
from huggingface_hub import login
from agents.scraping.scrapingTool2 import wiki_search
from agents.scraping.scrapingTool1 import scrape_wiki_from_url
from transformers import AutoTokenizer
import os
import shutil


# login("")

def list_topics(url_list):
    topic_list = []
    for url in url_list:
        topic = url.split('/')[-1]
        topic_list.append(topic)
    return topic_list

def user_input():
    keyword = input("Enter the topic: ")
    result = wiki_search(keyword)
    topic_list = list_topics(result["related_links"])
    print("______________________________________________")
    print(topic_list)
    print("______________________________________________")
    model(keyword, topic_list)


def generate_data(keyword, result, related_topics):
    output_folder = "agents/scraping/output_data"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(output_folder):
        file_path = os.path.join(output_folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

    keyword_file_path = os.path.join(output_folder, f"{keyword}.txt")
    with open(keyword_file_path, "w", encoding="utf-8") as file:
        file.write(result["content"])

    topics_to_links = []
    lot = related_topics.split(", ")
    for topic in lot:
        topics_to_links.append("https://en.wikipedia.org/wiki/" + topic)

    print(topics_to_links)

    for topic, link in zip(lot, topics_to_links):
        try:
            content = scrape_wiki_from_url(link)
            topic_file_path = os.path.join(output_folder, f"{topic}.txt")
            with open(topic_file_path, "w", encoding="utf-8") as file:
                file.write(content)
        except Exception as e:
            print(f"Failed to scrape or save content for topic '{topic}' from link '{link}'. Reason: {e}")

    print("Data generated successfully.")


def flow(keyword):
    result = wiki_search(keyword)
    topic_list = list_topics(result["related_links"])
    related_topics = model(keyword, topic_list)
    generate_data(keyword, result, related_topics)


def model(topic, topic_list):
    model_id = "meta-llama/Llama-3.2-1B-Instruct"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=torch.bfloat16,
        device_map="auto"
    )

    input_prompt = (
        f"You are a research assistant chatbot whose only purpose is to choose the five most relevant topics "
        f"from a list given the keyword '{topic}'. You will return them in a list separated with commas, "
        f"and nothing else should be in your response.\n\nTopics: {', '.join(topic_list)}\nResponse:"
    )

    input_ids = tokenizer(input_prompt, return_tensors="pt").input_ids.to(model.device)

    outputs = model.generate(
        input_ids=input_ids,
        max_new_tokens=256,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.2
    )

    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    related_topics = generated_text.replace(input_prompt, "").strip()

    print(f"Generated Topics: {related_topics}")
    return related_topics


if __name__ == "__main__":
    user_input()