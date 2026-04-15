from loader import load_data
from chunking import chunk_text
from embedding import create_embeddings

def store_embeddings(embeddings):
    # simple in-memory storage
    database = embeddings
    return database


def search(query, database):
    # simple similarity: closest length
    query_len = len(query)
    
    best_match = None
    min_diff = float('inf')
    
    for chunk, emb in database:
        diff = abs(emb - query_len)
        
        if diff < min_diff:
            min_diff = diff
            best_match = chunk
    
    return best_match


if __name__ == "__main__":
    text = load_data("data/sample.txt")
    chunks = chunk_text(text)
    embeddings = create_embeddings(chunks)
    
    db = store_embeddings(embeddings)
    
    query = "What is RAG?"
    result = search(query, db)
    
    print("\nQuery:", query)
    print("\nBest Match:", result)