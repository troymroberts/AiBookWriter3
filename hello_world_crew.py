from crewai import Agent, Task, Crew, Process
from langchain_ollama import Ollama
import os

# Define your Ollama LLM
ollama_llm = Ollama(
    base_url="http://10.1.1.47:11434",  # Your Ollama server's URL
    model="ollama/qwen2:1.5b",  # Include 'ollama/' prefix
    verbose=True,
)

# Create a simple agent
agent = Agent(
    role="Tester",
    goal="Test the connection to the Ollama server",
    backstory="An AI agent designed to verify connectivity.",
    llm=ollama_llm,
    verbose=True,
)

# Create a simple task with expected_output
task = Task(
    description="Say 'Hello, World!'",
    agent=agent,
    expected_output="The phrase 'Hello, World!' as a simple greeting.",
)

# Instantiate your crew
crew = Crew(
    agents=[agent],
    tasks=[task],
    process=Process.sequential,
    verbose=2,
)

# Run the crew
result = crew.kickoff()

print("######################")
print("Crew Result:")
print(result)