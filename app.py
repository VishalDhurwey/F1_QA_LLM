import os
import ollama
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from tqdm import tqdm


# ✅ Load and chunk the dataset
def load_text_chunks(file_path, chunk_size=1000, overlap=200):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

# ✅ Load embedding model
print("🔄 Loading embedding model...")
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# ✅ Load and embed chunks
chunks = load_text_chunks("data/f1_knowledge.txt")
print(f"✅ Loaded {len(chunks)} chunks.")

print("🔄 Generating embeddings...")
embeddings = embedding_model.encode(chunks, show_progress_bar=True)

# ✅ Build FAISS index
index = faiss.IndexFlatL2(embeddings[0].shape[0])
index.add(np.array(embeddings))


# ✅ Function to ask LLM using local Ollama
def query_ollama(prompt, model="llama2"):
    response = ollama.chat(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response['message']['content']


# ✅ Q&A function
def ask_f1_question(question, top_k=3):
    question_embedding = embedding_model.encode([question])
    distances, indices = index.search(np.array(question_embedding), top_k)
    context = "\n".join([chunks[i] for i in indices[0]])

    prompt = f"""Use the context below to answer the question.

Context:
{context}

Question: {question}
Answer:"""

    return query_ollama(prompt)


# ✅ Run CLI
print("🏁 F1 Vector QA (FAISS + Ollama) is ready! Type 'exit' to quit.\n")
while True:
    query = input("Ask anything about F1 ➤ ")
    if query.lower() == "exit":
        break
    answer = ask_f1_question(query)
    print(f"\n🧠 Answer:\n{answer.strip()}\n")