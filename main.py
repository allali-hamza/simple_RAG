import ollama
from src.rag import retrieve
from src.config import LANGUAGE_MODEL

input_query = input("ask me a question: ")
retrieved_knowledge = retrieve(input_query)

instruction_prompt = f'''You are a helpful chatbot.
Use only the following pieces of context to answer the question. Don't make up any new information:
{'\n'.join([f' - {chunk}' for chunk in retrieved_knowledge])}
'''

stream = ollama.chat(
    model=LANGUAGE_MODEL,
    messages=[
        {'role': 'system', 'content': instruction_prompt},
        {'role': 'user', 'content': input_query}
    ],
    stream=True,
)    
for part in stream:
    print(part["message"]["content"], end="", flush=True)

print()
