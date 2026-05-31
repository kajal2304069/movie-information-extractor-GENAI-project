from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.9
)

messages = [
    SystemMessage(content="You are a funny AI agent")
]

print("------- Welcome, type 0 to exit the application -------")

while True:
    prompt = input("You: ")

    if prompt == "0":
        break

    messages.append(HumanMessage(content=prompt))

    response = model.invoke(messages)

    messages.append(AIMessage(content=response.content))

    print("Bot:", response.content)

print(messages)
