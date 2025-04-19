from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

loader = TextLoader(file_path="campusX/langchain/document_loader/cricket.txt", encoding='utf-8')

docs = loader.load()

print(type(docs))
print(docs[0])

model= ChatGoogleGenerativeAI(model="gemini-1.5-pro")

prompt = PromptTemplate(
    template="Write a summary of the following poem - \n {poem}",
    input_variables=['poem']
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'poem' : docs[0].page_content})

print(result)