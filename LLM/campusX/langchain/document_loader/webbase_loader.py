from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader, WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

url = "https://www.amazon.de/-/en/Wireless-Bluetooth-Headphones-Integration-Algorithm/dp/B0CXPRHTNB/ref=sr_1_4?crid=1FENDC9JMXJPM&dib=eyJ2IjoiMSJ9.9IrOmKquKr1eRvfwr1RsUg4lPbMs8mFxXiYJ5ZSMQZjOKWcgBdX9fj82I3DsMB6suuym0oX3imVQvqvWej-fXtlUJDsMkGjEuZucnYwvMXi26EIGmUusR5OP9bVH4-7F7n03CQRDJ3P-EZfh-iKG3SGUAiWDG3_oE1OCi9xTcKVSxChOV6Mf239tszQWAp5UaVhv8BKmwDRSKL4aQmLLibq0o0kbJpsRXslcMcOKTL8.HdMWzI6Gy1pLMZPrxIrAY2cyWm6uV7IsUMJsOty4330&dib_tag=se&keywords=nothing%2Bear&qid=1745080590&sprefix=nothing%2Caps%2C89&sr=8-4&th=1"

loader = WebBaseLoader(url)

docs = loader.load()

# print(len(docs))
# print(docs[0].page_content)

model= ChatGoogleGenerativeAI(model="gemini-1.5-pro")

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

chain = prompt | model | parser

print(chain.invoke({'question':'What is the prodcut that we are talking about?', 'text':docs[0].page_content}))