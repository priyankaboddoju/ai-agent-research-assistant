class PlannerAgent:

    def create_plan(self, query):

        plan = [
            f"Search information about: {query}",
            "Analyze gathered information",
            "Generate final research summary"
        ]

        return plan