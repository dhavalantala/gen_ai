from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()

model= ChatGoogleGenerativeAI(model="gemini-1.5-pro")

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

def word_counter(text):
    return len(text.split())

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parelle_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'word_count' : RunnableLambda(word_counter)
})

# parelle_chain = RunnableParallel({
#     'joke' : RunnablePassthrough(),
#     'word_count' : RunnableLambda(lambda x:len(x.split()))
# })

final_chain = RunnableSequence(joke_gen_chain, parelle_chain)

result = final_chain.invoke({'topic' : "Cricket"})
print(result)

final_result = "{} \n word count {}".format(result['joke'], result['word_count'])
print(final_result)