# Load document from PDFs and TXT files
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_community.document_loaders.text import TextLoader
from langchain_community.document_loaders.directory import DirectoryLoader

# Load the text file from the given directory
pdf_loader = DirectoryLoader("./docs", glob=["*.pdf"],
                         loader_cls=PyPDFLoader,
                         loader_kwargs= {"mode" : "single"})

text_loader = DirectoryLoader("./docs", glob=["*.txt"],
                         loader_cls=TextLoader
                          )
# Load the documents
pdf_docs = pdf_loader.load()
text_docs = text_loader.load()

docs = pdf_docs + text_docs 

print("Loaded Documents :", len(docs))

# Print the loaded documents
# for doc in docs:
#     # Print the first 50 characters of each document
#     print(doc.page_content[:50])
#     print("-" * 50)
