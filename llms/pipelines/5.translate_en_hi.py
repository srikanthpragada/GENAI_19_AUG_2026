from transformers import pipeline
from transformers import logging
logging.set_verbosity_error()

translator = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-3B-Instruct"
)

prompt = """
Translate English to Hindi. Give no more details.

How are you today?
"""

result = translator(prompt, return_full_text=False)

print(result[0]["generated_text"])
