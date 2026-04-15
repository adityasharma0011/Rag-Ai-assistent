from loader import load_data
from chunking import chunk_text
from retrieve import simple_retriever

def generate_answer(query, context):
    # simple rule-based generator (dummy LLM)
    answer = f"Based on the document, {context}"
    return answer


if __name__ == "__main__":
    text = load_data("data/sample.txt")
    chunks = chunk_text(text)
    
    query = "What is RAG?"
    
    context = simple_retriever(query, chunks)
    
    answer = generate_answer(query, context)
    
    print("\nQuery:", query)
    print("\nRetrieved Context:", context)
    print("\nFinal Answer:", answer)