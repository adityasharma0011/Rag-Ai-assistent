from loader import load_data

def chunk_text(text, chunk_size=50, overlap=10):
    chunks = []
    
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        
        start += chunk_size - overlap   # overlap logic
    
    return chunks


if __name__ == "__main__":
    text = load_data("data/sample.txt")
    
    chunks = chunk_text(text)
    
    for i, chunk in enumerate(chunks):
        print(f"\nChunk {i+1}:")
        print(chunk)