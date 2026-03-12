import requests
from tools.web_search import search_web

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"

def research_agent(query: str) -> str:
    # get web results
    web_results = search_web(query)

    prompt = f"""
You are an AI research assistant.

User question:
{query}

Relevant web information:
{web_results}

Provide a clear and concise answer.
"""

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    result = response.json()

    return result["response"]