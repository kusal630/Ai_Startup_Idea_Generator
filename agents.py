from llm import generate

class Agent:
    def __init__(self, role, goal):
        self.role = role
        self.goal = goal

    def act(self, task):
        prompt = f"""
        Role: {self.role}
        Goal: {self.goal}
        Task: {task}
        Give structured output.
        """
        return generate(prompt)


idea_generator = Agent(
    "Startup Idea Generator",
    "Generate innovative AI startup ideas"
)

market_researcher = Agent(
    "Market Researcher",
    "Analyze market demand and competitors"
)

business_strategist = Agent(
    "Business Strategist",
    "Create business models"
)

pitch_creator = Agent(
    "Pitch Creator",
    "Create compelling startup pitch"
)