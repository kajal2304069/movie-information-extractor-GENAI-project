from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash"
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("What is deepseek?")
print(response.content)
