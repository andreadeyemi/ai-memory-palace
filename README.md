# 🧠 AI Memory Palace

> _"We don’t forget code. We forget who we were becoming."_

![Python](https://img.shields.io/badge/python-3.10-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![GPT-3.5](https://img.shields.io/badge/GPT-powered-brightgreen)
![Embeddings](https://img.shields.io/badge/semantic-memory-orange)

---

## 📖 Backstory

This project began with one question:  
**“What if your thoughts could think back?”**

Note-taking apps save.  
This system **recalls, summarizes, and classifies.**

Built for those who move in silence, think in layers, and build in clarity.

---

## 📌 Overview

**AI Memory Palace** is a GPT-powered cognitive engine that captures thoughts, ideas, and lessons into vector memory —  
then retrieves and summarizes them using LLMs.

Inspired by **neural recall**, optimized for **mental discipline**, and powered by **embeddings + GPT-3.5**.

---

## 🔧 Key Features

| Feature                    | Description                                          |
|----------------------------|------------------------------------------------------|
| 🔍 Semantic Recall         | Retrieve ideas by meaning, not just keywords         |
| 🧠 GPT-3.5 Intelligence    | Auto-tags thoughts + summarizes answers              |
| 🧰 Terminal CLI            | Save/search with blazing speed via command line     |
| 🧬 Vector Embeddings       | SentenceTransformer for deep understanding           |
| 🔐 .env Protected Keys     | Secure OpenAI access without hardcoding              |

---

## 🧠 How It Works

### Save a memory

```bash
python main.py save "Discipline hurts now, but it saves later."
Retrieve and summarize with GPT
bash
Copy
Edit
python main.py search "What is discipline?" --summarize
Output
rust
Copy
Edit
1. 🧠 Discipline hurts now, but it saves later. (lesson) [score: 0.91]

🧠 Summary:
You've internalized discipline as delayed relief — pain now, freedom later.
🧪 Memory Flow (Visual)
css
Copy
Edit
Thought → [Embedder] → [Vector Vault] → 🧠
                        ↑
        [GPT: Tag + Summarize]
🔍 Why This Over a Notes App?
Feature	Notes App	AI Memory Palace
Keyword search only	✅	✅
Semantic meaning search	❌	✅
GPT-powered summaries	❌	✅
Auto-tagging via AI	❌	✅
Embedding & vector logic	❌	✅

🚀 Quickstart
1. Clone this repo
bash
Copy
Edit
git clone https://github.com/yourname/ai-memory-palace
cd ai-memory-palace
2. Create .env file with your OpenAI key
env
Copy
Edit
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run it
bash
Copy
Edit
python main.py save "I grow when it's hardest."
python main.py search "What helps me grow?" --summarize
🛠 File Structure
graphql
Copy
Edit
ai-memory-palace/
├── main.py               # CLI for memory save/search
├── memory_engine.py      # Embedding + retrieval logic
├── llm_classifier.py     # GPT-based memory categorizer
├── llm_summarizer.py     # GPT-based memory summarizer
├── memory_db.json        # Your private memory vault
├── .env                  # Local OpenAI key file (never upload)
├── .gitignore            # Keeps secrets private
└── requirements.txt      # Fast setup
🧬 Built For
Engineers building mental discipline

Founders organizing legacy

Writers capturing insight

Builders tracking inner philosophy

Developers training AI on their own mind

🛣 Roadmap
 Streamlit dashboard (visual interface)

 Notion + Markdown export

 Timeline replay mode

 Memory decay + importance weighting

 Plugin system for journals, dreams, habits

⚖️ License
MIT — use it, remix it, but build something timeless.

