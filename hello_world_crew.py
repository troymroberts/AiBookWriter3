from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama

# Define your Ollama LLM
ollama_llm = Ollama(
    base_url="http://10.1.1.47:11434",
    model="qwen2:1.5b",
)

# Create a simple agent
agent = Agent(
    role="Writer",
    goal="Write a simple hello world message",
    backstory="An AI agent that specializes in writing short messages.",
    llm=ollama_llm,
    verbose=True,  # Set verbose to True to see the agent's inner monologue
)

# Create a task for the agent
task = Task(
    description="Write a single 'Hello, World!' message.",
    agent=agent,
)

# Instantiate your crew with a sequential process
crew = Crew(
    agents=[agent],
    tasks=[task],
    process=Process.sequential,
    verbose=2,  # Set verbose to 2 to see the crew's tasks
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print("Crew Work Result:")
print(result)