# AI Agent Research Assistant

A lightweight **AI-powered research assistant** built with Python and local LLMs using Ollama.
The agent can search the web, analyze results, and generate research-style answers.

This project demonstrates the architecture of a **tool-using AI agent system** and serves as a foundation for building more advanced AI agents with planning, memory, and multi-agent collaboration.

---

# Features

* Local LLM inference using Ollama
* Web search integration
* Modular AI agent architecture
* Planner Agent for task breakdown
* Tool-based reasoning workflow
* Lightweight and fully local setup

---

# Project Architecture

The system follows a **multi-step AI agent workflow**.

```
User Query
   │
   ▼
Planner Agent
   │
   ▼
Research Agent
   │
   ▼
Web Search Tool
   │
   ▼
Ollama LLM
   │
   ▼
Generated Answer
```

### Planner Agent

Breaks the user query into structured research steps.

Example:

```
User Query:
What is Meditation?

Research Plan:
- Search information about Meditation
- Analyze gathered information
- Generate final research summary
```

### Research Agent

Collects web search results and uses the LLM to generate a structured response.

---

# Project Structure

```
ai-agent-research-assistant
│
├── agents
│   ├── planner_agent.py
│   └── research_agent.py
│
├── tools
│   └── web_search.py
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

Example interaction:

```
Ask Research Question: What is Meditation?

Research Plan:
- Search information about: What is Meditation?
- Analyze gathered information
- Generate final research summary

Searching the web...
Analyzing information with AI...

Research Result:
Meditation is a mind-body practice that involves training attention and awareness to cultivate a calm and focused state of mind.
```

---

# Technologies Used

* Python
* Ollama
* Local LLMs
* DuckDuckGo Web Search
* AI Agent Architecture

---

# Future Improvements

* Conversation memory
* Multi-agent collaboration system
* Web interface using Streamlit
* Task planning agents
* Document-based research
* Streaming LLM responses

---

# Author

Priyanka Boddoju
MS Data Science – University of New Haven

GitHub
https://github.com/priyankaboddoju
