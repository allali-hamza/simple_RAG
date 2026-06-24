from src.embeddings import embeddings

VECTOR_DB = []

for item in embeddings:
    VECTOR_DB.append((item[0], item[1]["embeddings"][0]))

if __name__ == "__main__":
    for chuck, embedding in VECTOR_DB:
        print(chuck)
        print(embedding)
        print(len(embedding))
        break