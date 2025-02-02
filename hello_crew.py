from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama

# Define the Ollama LLM instance
ollama_llm = Ollama(model="qwen2.5:1.5b", base_url="http://10.1.1.47:11434")

# Create a simple agent
agent = Agent(
    role='Test Agent',
    goal='Say hello and confirm connection to Ollama',
    backstory='An agent designed to test connectivity.',
    verbose=True,  # See what the agent is doing
    llm=ollama_llm
)

# Create a simple task
task = Task(
    description='Simply say "Hello World" from Ollama.',
    agent=agent
)

# Create a crew with a single agent and task
crew = Crew(
    agents=[agent],
    tasks=[task],
    process=Process.sequential,  # Tasks are done one after another
    verbose=2  # See details about the crew's execution
)

# Run the crew and get the result
result = crew.kickoff()

# Print the result
print("Crew Result:")
print(result)