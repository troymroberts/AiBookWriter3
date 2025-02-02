import logging
from crewai import Agent, Task, Crew, Process

# Configure logging (optional)
logging.basicConfig(level=logging.DEBUG)

# Create a simple agent
agent = Agent(
    role='Test Agent',
    goal='Say hello and confirm connection to Ollama',
    backstory='An agent designed to test connectivity.',
    verbose=True,
    llm_model='ollama/qwen2.5:1.5b',
    llm_base_url="http://10.1.1.47:11434"
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