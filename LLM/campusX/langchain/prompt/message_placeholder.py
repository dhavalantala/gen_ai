from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Chat template
chat_template = ChatPromptTemplate([
    ('system', 'you are helpful customer support agent'),
    MessagesPlaceholder(variable_name="chat_history"),
    ('human', '{query}')
])

chat_history = []

# Load Chat history
with open("campusX/langchain/prompt/chat_history.txt") as f:
    chat_history.extend(f.readlines())
# print(chat_history)

# Create  Prompt
prompt = chat_template.invoke({"chat_history" : chat_history, 'query' : "Where is my refund?"})

print(prompt)


