
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import OpenAIEmbeddings
embeddings=OpenAIEmbeddings(
  model="text_embedding-3-large",
  dimensions=64
)
vector=embeddings.embed_query("you are going to learn gen ai")
print(vector)
