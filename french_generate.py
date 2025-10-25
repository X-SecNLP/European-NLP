from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# --- French Model Loading (Tiniest Version: GPT-2 French Small) ---
# Model ID for the tiny French Causal LLM (~100M parameters)
model_id_tiny_fr = "dbddv01/gpt2-french-small"
print(f"Loading tiny French Model: {model_id_tiny_fr}...")

# Load the tokenizer and model
tokenizer_fr_tiny = AutoTokenizer.from_pretrained(model_id_tiny_fr)

# Use GPT2ForCausalLM class since the model is a fine-tuned GPT-2
model_fr_tiny = AutoModelForCausalLM.from_pretrained(model_id_tiny_fr)

# Set the device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_fr_tiny.to(device)

# --- French Sentence Completion and Prediction ---

# 1. Define the French Prompt
# Starting a story or a description
french_prompt_tiny = "La Tour Eiffel, construite pour l'Exposition Universelle de 1889, est devenue le symbole de Paris. Chaque année, des millions de visiteurs" 
# Translation: The Eiffel Tower, built for the 1889 World's Fair, has become the symbol of Paris. Every year, millions of visitors... (Model is expected to suggest a continuation)

# 2. Encode the Prompt
input_ids_fr_tiny = tokenizer_fr_tiny.encode(
    french_prompt_tiny, 
    return_tensors="pt"
).to(device)

# 3. Use the Model to Generate Text
# Setting max_new_tokens very low for extremely fast inference
output_fr_tiny = model_fr_tiny.generate(
    input_ids_fr_tiny,
    max_new_tokens=30,             # Generate max 30 new tokens
    do_sample=True,                # Enable sampling
    temperature=0.7,               # Control randomness
    top_k=50,                      
    # GPT-2 models typically use the EOS token for padding
    pad_token_id=tokenizer_fr_tiny.eos_token_id 
)

# 4. Decode the Generated Tokens
generated_text_fr_tiny = tokenizer_fr_tiny.decode(
    output_fr_tiny[0], 
    skip_special_tokens=True
)

# 5. Print the Results
print("-" * 50)
print(f"Model ID: {model_id_tiny_fr}")
print(f"Input French Prompt:\n{french_prompt_tiny}")
print("-" * 50)
print(f"Complete Generated Text (French):\n{generated_text_fr_tiny}")
print("-" * 50)