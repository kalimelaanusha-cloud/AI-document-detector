import chromadb


# Create a local ChromaDB database
client = chromadb.PersistentClient(path="./chroma_db")


# Create or get our document collection
collection = client.get_or_create_collection(
    name="documents"
)


def add_document(document_id, text, embedding):
    collection.add(
        ids=[document_id],
        documents=[text],
        embeddings=[embedding.tolist()]
    )


def search_documents(embedding, number_of_results=3):
    results = collection.query(
        query_embeddings=[embedding.tolist()],
        n_results=number_of_results
    )

    return results


if __name__ == "__main__":
    print("Database is working!")
    print("Collection:", collection.name)