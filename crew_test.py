import os
from crewai import Agent, Crew, Task, Process

# Step 1: Set the base URL for Ollama as an environment variable
os.environ["OLLAMA_API_BASE"] = "http://10.1.1.47:11434"

# Create a very basic agent
researcher = Agent(
    role="Researcher",
    goal="Answer a simple question",
    backstory="An AI agent designed to answer basic questions.",
    verbose=True,
    allow_delegation=False,
    llm_model="ollama/qwen2.5:1.5b"  # Using direct model name instead of LLM instance
)

# Create a simple task
task = Task(
    description="What is the capital of France?",
    agent=researcher,
    expected_output="A clear statement indicating that Paris is the capital of France."
)

# Create a crew with the agent and task
crew = Crew(
    agents=[researcher],
    tasks=[task],
    process=Process.sequential,
    verbose=True
)

# Run the crew
try:
    result = crew.kickoff()
    print("Crew Result:", result)
except Exception as e:
    print(f"An error occurred: {str(e)}")
    raise