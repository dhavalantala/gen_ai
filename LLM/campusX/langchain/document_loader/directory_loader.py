from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

loader = DirectoryLoader(
    path="campusX/langchain/document_loader/book", ## Give a path of the directory
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.load()

# model= ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# parser = StrOutputParser()

# prompt = PromptTemplate()

# chain = prompt | model | parser