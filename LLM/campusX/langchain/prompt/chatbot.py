from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

chat_history = [
    SystemMessage(content="YOu are a helpful AI Assistant")
]

while True:
    user_input = input("you : ")
    chat_history.append(HumanMessage(content=user_input)) # type: ignore

    if user_input.lower() == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content)) # type: ignore
    print("AI: ", result.content)

print(chat_history)