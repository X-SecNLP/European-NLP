from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load the model and tokenizer
model_id = "LSX-UniWue/LLaMmlein_1B"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

# Set the device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

####

german_prompt = "Der beste Weg, ein Problem zu lösen, ist es zuerst zu verstehen, also" 

input_ids = tokenizer.encode(german_prompt, return_tensors="pt").to(device)
output = model.generate(
    input_ids,
    max_new_tokens=50,
    do_sample=True,
    temperature=0.7,
    top_k=50,
    pad_token_id=tokenizer.eos_token_id
)

generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print("-" * 50)
print(f"Model ID: {model_id}")
print(f"German Prompt: {german_prompt}")
print("-" * 50)
print(f"Generated Text:\n{generated_text}")
print("-" * 50)