import os
from crewai import Agent, Task, Crew
from langchain_community.llms import Ollama

# 1. Define your Ollama LLM
ollama_llm = Ollama(
    base_url='http://localhost:11434',
    model='qwen2.5:1.5b'
)

# 2. Create an Agent
hello_agent = Agent(
    role='Greeting Agent',
    goal='Say hello to the user in a friendly way.',
    backstory="A simple agent designed to greet users.",
    llm=ollama_llm,  # Assign the Ollama LLM to the agent
    verbose=True  # Set to True for more detailed output during execution
)

# 3. Create a Task for the Agent
hello_task = Task(
    description='Greet the user with a simple "Hello World!" message.',
    agent=hello_agent
)

# 4. Create a Crew and Assign the Task
hello_crew = Crew(
    agents=[hello_agent],
    tasks=[hello_task],
    verbose=2  # Set to 2 for even more detailed crew execution output
)

# 5. Run the Crew and Get the Result
result = hello_crew.kickoff()

print("\nCrew Result:")
print(result)