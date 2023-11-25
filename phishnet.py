"""
This module uses GPT-2 from Hugging Face's transformers library to generate text based on a prompt.
"""

from transformers import GPT2Tokenizer, GPT2LMHeadModel

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

PROMPT_TEXT = "Urgent: Your account has been compromised"

inputs = tokenizer.encode(PROMPT_TEXT, add_special_tokens=False, return_tensors='pt')
outputs = model.generate(
    inputs,
    max_length=100,
    num_return_sequences=1,
    temperature=0.7,
    top_p=0.9,
    do_sample=True,
    no_repeat_ngram_size=2
)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
