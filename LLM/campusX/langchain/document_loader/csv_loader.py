from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader, CSVLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

loader = CSVLoader(file_path='campusX/langchain/document_loader/dt/Social_Network_Ads.csv')

docs = loader.load()

print(len(docs))
print(docs[1])

# model= ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# parser = StrOutputParser()

# prompt = PromptTemplate()

# chain = prompt | model | parser