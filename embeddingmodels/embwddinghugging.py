
from dotenv import load_dotenv
load_dotenv()
from sentence_transformers import SentenceTransformer

print("Loading model...")

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

print("Model loaded!")

embeddings = model.encode([
    "Hello this is kajal",
    "Hello youtube channel"
])

print(embeddings.shape)
