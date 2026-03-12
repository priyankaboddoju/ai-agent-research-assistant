from langchain_community.llms import Ollama
from langchain.agents import initialize_agent, Tool
from tools.web_search import search_web

llm = Ollama(model="llama3")

tools = [
    Tool(
        name="WebSearch",
        func=search_web,
        description="Search the internet for recent information"
    )
]

research_agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True
)