# llm_summarizer.py

import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_memories(memories, query):
    if not memories:
        return "No relevant memories found."

    context = "\n".join([f"- {m['thought']}" for m in memories])

    prompt = f"""
You are a helpful assistant. Summarize the key insights from the user's memory logs based on their question.

Question: "{query}"

Memories:
{context}

Answer:
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()
