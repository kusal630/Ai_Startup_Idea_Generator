from agents import idea_generator, market_researcher, business_strategist, pitch_creator

def run(topic):
    idea = idea_generator.act(f"Generate a startup idea in {topic}")
    
    research = market_researcher.act(
        f"Analyze this idea:\n{idea}"
    )
    
    strategy = business_strategist.act(
        f"Create business plan for:\n{idea}"
    )
    
    pitch = pitch_creator.act(
        f"Create pitch for:\n{idea}\n{strategy}"
    )

    return f"""
================= FINAL OUTPUT =================

IDEA:
{idea}

-----------------------------------------------

MARKET RESEARCH:
{research}

-----------------------------------------------

STRATEGY:
{strategy}

-----------------------------------------------

PITCH:
{pitch}

================================================
"""


if __name__ == "__main__":
    topic = input("Enter domain: ")
    print(run(topic))