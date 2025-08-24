# memory_engine.py

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json
import uuid

# Load transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Local memory store
MEMORY_FILE = "memory_db.json"

def embed_text(text):
    return model.encode([text])[0].tolist()

def save_memory(thought, metadata=None):
    memory = {
        "id": str(uuid.uuid4()),
        "thought": thought,
        "vector": embed_text(thought),
        "metadata": metadata or {}
    }

    try:
        with open(MEMORY_FILE, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(memory)

    with open(MEMORY_FILE, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"✅ Memory saved: {thought[:60]}...")

def search_memory(query, top_k=3):
    query_vec = embed_text(query)

    with open(MEMORY_FILE, 'r') as f:
        data = json.load(f)

    vectors = np.array([item['vector'] for item in data])
    sims = cosine_similarity([query_vec], vectors)[0]

    top_indices = np.argsort(sims)[-top_k:][::-1]

    for i in top_indices:
        item = data[i]
        print(f"🧠 {item['thought']}  (score: {sims[i]:.2f})\n")

