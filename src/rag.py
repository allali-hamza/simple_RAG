import ollama
from src.config import EMBEDDING_MODEL
from src.vector_store import VECTOR_DB
from src.cosine_similarity import cosine_simil



#the retrieval function 
def retrieve(query, top_n=3):
    query_embedding = ollama.embed(model=EMBEDDING_MODEL, input=query)
    similarities = []

    for chunk, embedding in VECTOR_DB:
        similarity = cosine_simil(query_embedding["embeddings"][0], embedding)
        similarities.append((similarity, chunk))

    sorted_similarities = sorted(similarities, key=lambda x: x[0], reverse=True)
    return [chunk for sim, chunk in sorted_similarities[:top_n]]

if __name__ == "__main__":
    query = "Female cats tend to do something"
    print(retrieve(query=query))
