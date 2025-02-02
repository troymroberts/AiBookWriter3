from crewai import Agent, Crew, Task, Process
from langchain_community.llms import Ollama

# Initialize Ollama LLM
ollama = Ollama(
    base_url="http://10.1.1.47:11434",
    model="qwen2.5:1.5b"
)

# Create a very basic agent
researcher = Agent(
    role="Researcher",
    goal="Answer a simple question",
    backstory="An AI agent designed to answer basic questions.",
    verbose=True,
    allow_delegation=False,
    llm=ollama  # Pass the Ollama LLM instance directly
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

# Run the crew with better error handling
try:
    result = crew.kickoff()
    print("Crew Result:", result)
except Exception as e:
    print(f"An error occurred: {str(e)}")
    import traceback
    traceback.print_exc()  # This will print the full error trace