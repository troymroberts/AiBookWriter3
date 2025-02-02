from crewai import Agent, Crew, Task, Process
from langchain_community.llms import Ollama

# Define your Ollama LLM (replace with your server's details)
ollama_llm = Ollama(
    base_url="http://10.1.1.47:11434",  # Replace with your Ollama server URL
    model="qwen2.5:1.5b",  # Replace with your desired model
    temperature=0.7,
)

# Create a very basic agent
researcher = Agent(
    role="Researcher",
    goal="Answer a simple question",
    backstory="An AI agent designed to answer basic questions.",
    verbose=True,
    llm=ollama_llm,
)

# Create a simple task
task = Task(
    description="What is the capital of France?",
    agent=researcher,
)

# Create a crew with the agent and task
crew = Crew(
    agents=[researcher],
    tasks=[task],
    process=Process.sequential,
    verbose=True,
)

# Run the crew
result = crew.kickoff()

# Print the result
print("Crew Result:", result)