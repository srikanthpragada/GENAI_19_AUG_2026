from transformers.utils import logging
import warnings

warnings.filterwarnings("ignore")
logging.set_verbosity_error()
logging.disable_progress_bar()

from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline

pipe = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-3B-Instruct",
)

llm = HuggingFacePipeline(pipeline=pipe)

print(llm.invoke("Who created Python Language?"))
