# Ai_Startup_Idea_Generator
A multi-agent AI system built with CrewAI that takes a raw topic or industry and produces a fully structured startup concept — from ideation to a pitch-ready output. Built as part of the IIT Jammu Winter School on AI Agents.

Overview
This project demonstrates real-world multi-agent collaboration using CrewAI. Four specialized agents work in a sequential pipeline, where each agent's output feeds into the next — mimicking how a real startup founding team would operate.

Agent Architecture
text
User Input (Industry / Problem Statement)
        │
        ▼
┌─────────────────────┐
│   Idea Generator    │  Generates innovative startup concepts based on the input
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│  Market Researcher  │  Validates demand, identifies competitors, estimates market size
└─────────┬───────────┘
          │
          ▼
┌──────────────────────┐
│ Business Strategist  │  Defines revenue model, target audience, and go-to-market strategy
└─────────┬────────────┘
          │
          ▼
┌─────────────────────┐
│   Pitch Creator     │  Crafts a compelling investor pitch from all previous outputs
└─────────────────────┘
          │
          ▼
   Structured Output
Agents & Roles
Agent	Role	Responsibility
Idea Generator	Creative Lead	Generates 3–5 innovative startup concepts based on the given domain
Market Researcher	Research Analyst	Validates market demand, identifies competitors, estimates TAM/SAM
Business Strategist	Strategy Lead	Designs revenue model, pricing, target persona, and growth strategy
Pitch Creator	Communications Lead	Synthesizes all outputs into a structured investor pitch narrative
Tech Stack
CrewAI — Multi-agent orchestration framework

Python 3.10+

OpenAI API / Groq / Ollama — LLM backbone (configurable)
