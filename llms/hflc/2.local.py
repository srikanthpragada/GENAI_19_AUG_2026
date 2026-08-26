from transformers.utils import logging
import warnings

warnings.filterwarnings("ignore")
logging.set_verbosity_error()
logging.disable_progress_bar()


from langchain_huggingface import HuggingFacePipeline


llm = HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen2.5-3B-Instruct",
    task="text-generation" 
)

print(llm.invoke("Who created Python Language"))
