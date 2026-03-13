from agents.research_agent import research_agent
from agents.planner_agent import PlannerAgent

planner = PlannerAgent()

while True:
    query = input("\nAsk Research Question: ")

    if query.lower() == "exit":
        break

    # Create research plan
    plan = planner.create_plan(query)

    print("\nResearch Plan:")
    for step in plan:
        print("-", step)

    # Run research
    result = research_agent(query)

    print("\nResearch Result:\n")
    print(result)