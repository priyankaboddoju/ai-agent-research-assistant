from agents.research_agent import research_agent

while True:
    query = input("\nAsk Research Question: ")

    if query.lower() == "exit":
        break

    result = research_agent(query)

    print("\nResearch Result:\n")
    print(result)