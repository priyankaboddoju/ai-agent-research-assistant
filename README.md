# AI Agent Research Assistant

A lightweight **AI-powered research assistant** built with Python and local LLMs using Ollama.
The agent can search the web, analyze results, and generate research-style answers.

This project demonstrates the architecture of a **tool-using AI agent system** and serves as a foundation for building more advanced AI agents with planning, memory, and multi-agent collaboration.

---

# Features

* Local LLM inference using Ollama
* Web search integration
* Modular AI agent architecture
* Tool-based reasoning workflow
* Lightweight and fully local setup

---

# Project Architecture

```
User Query
   │
   ▼
Research Agent
   │
   ▼
Search Tool
   │
   ▼
Ollama LLM
   │
   ▼
Generated Answer
```

---

# Project Structure

```
ai-agent-research-assistant
│
├── agents
│   └── research_agent.py
│
├── tools
│   └── search_tool.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Installation

## 1 Install Ollama

Download and install Ollama:

https://ollama.ai

---

## 2 Pull a model

Run:

```
ollama run llama3
```

This downloads and runs the Llama3 model locally.

---

## 3 Clone the repository

```
git clone https://github.com/priyankaboddoju/ai-agent-research-assistant.git

cd ai-agent-research-assistant
```

---

## 4 Create a virtual environment

```
python -m venv venv
```

Activate it:

### Windows

```
venv\Scripts\activate
```

### Mac / Linux

```
source venv/bin/activate
```

---

## 5 Install dependencies

```
pip install -r requirements.txt
```

---

# Run the Agent

```
python main.py
```

Example prompt:

```
Research topic: AI agents
```

Example output:

```
AI agents are autonomous systems capable of performing tasks
by reasoning, planning, and using external tools such as search
engines or APIs.
```

---

# Technologies Used

* Python
* Ollama
* Local LLMs
* DuckDuckGo Search
* Modular AI Agent Architecture

---

# Future Improvements

* Multi-agent collaboration system
* Memory for conversation context
* Web interface using Streamlit
* Task planning agents
* Document research capabilities

---

# Author

Priyanka Boddoju
MS Data Science – University of New Haven

GitHub
https://github.com/priyankaboddoju
