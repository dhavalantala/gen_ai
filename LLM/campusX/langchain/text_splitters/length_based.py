from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("campusX/langchain/document_loader/dt/dl-curriculum.pdf")

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=5,
    separator=''
)

result = splitter.split_documents(docs)

print(result[0].page_content)
print("-------------------------")
print(result[1].page_content)