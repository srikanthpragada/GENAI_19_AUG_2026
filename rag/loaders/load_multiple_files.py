# Load document from Text File
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_community.document_loaders.directory import DirectoryLoader

# Load the text file from the given directory
loader = DirectoryLoader("./docs", glob=["*.pdf"],
                         loader_cls=PyPDFLoader,
                         loader_kwargs= {"mode" : "single"})

# Load the documents
docs = loader.load()
print("Loaded Documents :", len(docs))

# Print the loaded documents
for doc in docs:
    # Print the first 50 characters of each document
    print(doc.page_content[:50])
    print("-" * 50)
