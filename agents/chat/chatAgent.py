from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "meta-llama/Llama-3.2-1b"

device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16 if device == "cuda" else torch.float32,
    device_map="auto" if device == "cuda" else None
).to(device)

def chat(context):
    conversation_context = f"Context: {context}\n"
    print("Start QnA. Type '/exit' to end.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "/exit":
            break

        prompt = conversation_context + f"User: {user_input}\nAssistant:"
        input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(device)

        output = model.generate(
            input_ids=input_ids,
            max_new_tokens=200,
            temperature=0.7,
            top_p=0.9,
            pad_token_id=tokenizer.eos_token_id
        )

        response = tokenizer.decode(output[0], skip_special_tokens=True)
        response_text = response[len(prompt):].strip()
        print(f"Assistant: {response_text}")

        conversation_context += f"User: {user_input}\nAssistant: {response_text}\n"

        max_context_length = 4096
        if len(conversation_context) > max_context_length:
            conversation_context = conversation_context[-max_context_length:]

if __name__ == "__main__":
    initial_context = "Powerlifting is a strength sport focused on the squat, bench press, and deadlift."
    chat(initial_context)
