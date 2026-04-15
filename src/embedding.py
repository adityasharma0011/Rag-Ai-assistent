from loader import load_data
from chunking import chunk_text

def create_embeddings(chunks):
    embeddings = []
    
    for chunk in chunks:
        # simple dummy embedding
        vector = len(chunk)   # length as fake embedding
        embeddings.append((chunk, vector))
    
    return embeddings


if __name__ == "__main__":
    text = load_data("data/sample.txt")
    chunks = chunk_text(text)
    
    embeddings = create_embeddings(chunks)
    
    for i, (chunk, emb) in enumerate(embeddings):
        print(f"\nChunk {i+1}: {chunk}")
        print(f"Embedding: {emb}")