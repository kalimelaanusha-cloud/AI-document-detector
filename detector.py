from sentence_transformers import SentenceTransformer


# Load the AI model
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embedding(text):
    """
    Convert document text into a numerical embedding.
    """
    if not text.strip():
        raise ValueError("No text found in the document.")

    embedding = model.encode(text)

    return embedding


if __name__ == "__main__":
    test_text = "This is a test document for AI Document Detector."

    embedding = create_embedding(test_text)

    print("Detector is working!")
    print("Embedding created successfully.")
    print("Embedding size:", len(embedding))