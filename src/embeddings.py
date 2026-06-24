from src.config import EMBEDDING_MODEL
from src.loader import dataset
import ollama

chunks = []
for line in dataset:
    chunks.append(line)

embeddings = []
for chunk in chunks:
    emb = ollama.embed(model=EMBEDDING_MODEL, input=chunk)
    embeddings.append((chunk ,emb))


if __name__ == "__main__":
    print(embeddings[0])
