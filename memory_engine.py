# memory_engine.py

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json
import uuid

from llm_classifier import classify_thought
from llm_summarizer import summarize_memories

# Load transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Local memory store
MEMORY_FILE = "memory_db.json"

def embed_text(text):
    return model.encode([text])[0].tolist()

def save_memory(thought):
    tag = classify_thought(thought)

    memory = {
        "id": str(uuid.uuid4()),
        "thought": thought,
        "vector": embed_text(thought),
        "metadata": {"category": tag}
    }

    try:
        with open(MEMORY_FILE, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(memory)

    with open(MEMORY_FILE, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"✅ Saved ({tag}): {thought[:60]}...")

def search_memory(query, top_k=3, summarize=False):
    query_vec = embed_text(query)

    try:
        with open(MEMORY_FILE, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("🛑 No memory file found.")
        return

    if not data:
        print("🛑 Memory is empty.")
        return

    vectors = np.array([item['vector'] for item in data])
    sims = cosine_similarity([query_vec], vectors)[0]

    top_indices = np.argsort(sims)[-top_k:][::-1]
    results = [data[i] for i in top_indices]

    for i, item in enumerate(results):
        tag = item['metadata'].get('category', 'unknown')
        print(f"{i+1}. 🧠 {item['thought']} ({tag})  [score: {sims[top_indices[i]]:.2f}]")

    if summarize:
        print("\n🧠 Summary:")
        print(summarize_memories(results, query))


