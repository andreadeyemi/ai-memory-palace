# llm_classifier.py

import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def classify_thought(thought):
    prompt = f"""
Label this memory thought with ONE of these categories: "quote", "habit", "lesson", "dream", "reflection", "task".

Thought: "{thought}"

Only respond with the category.
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip().lower()
