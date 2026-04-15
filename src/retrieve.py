from loader import load_data
from chunking import chunk_text

def simple_retriever(query, chunks):
    best_match = None
    max_score = -1
    
    query_words = query.lower().split()
    
    for chunk in chunks:
        score = 0
        chunk_lower = chunk.lower()
        
        for word in query_words:
            if word in chunk_lower:
                score += 1
        
        if score > max_score:
            max_score = score
            best_match = chunk
    
    return best_match


if __name__ == "__main__":
    text = load_data("data/sample.txt")
    chunks = chunk_text(text)
    
    query = "What is RAG?"
    
    result = simple_retriever(query, chunks)
    
    print("\nQuery:", query)
    print("\nBest Match:", result)