import logging
from crewai import Agent, Task, Crew, Process
from langchain_ollama import OllamaLLM

# Configure logging to show DEBUG level messages (optional)
logging.basicConfig(level=logging.DEBUG)

# Define the Ollama LLM instance
ollama_llm = OllamaLLM(
    model="ollama/qwen2.5:1.5b",  # Specify "ollama/" prefix
    base_url="http://10.1.1.47:11434"
)

# Create a simple agent
agent = Agent(
    role='Test Agent',
    goal='Say hello and confirm connection to Ollama',
    backstory='An agent designed to test connectivity.',
    verbose=True,
    llm=ollama_llm
)

# Create a simple task
task = Task(
    description='Simply say "Hello World" from Ollama.',
    expected_output='The agent should output a greeting like "Hello World"',
    agent=agent
)

# Create a crew
crew = Crew(
    agents=[agent],
    tasks=[task],
    process=Process.sequential,
    verbose=True
)

# Run the crew
result = crew.kickoff()

# Print the result
print("Crew Result:")
print(result)