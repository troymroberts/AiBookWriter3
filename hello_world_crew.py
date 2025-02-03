import os
from crewai import Agent, Task, Crew
from langchain_ollama import OllamaLLM

# 1. Define your Ollama LLM with model_kwargs
ollama_llm = OllamaLLM(
    model='qwen2.5:1.5b',
    base_url='http://localhost:11434', # Keep base_url here as well for clarity
    model_kwargs={'base_url': 'http://localhost:11434', 'model': 'qwen2.5:1.5b'} # Explicitly in model_kwargs too
)

# 2. Create an Agent
hello_agent = Agent(
    role='Greeting Agent',
    goal='Say hello to the user in a friendly way.',
    backstory="A simple agent designed to greet users.",
    llm=ollama_llm,  # Assign the Ollama LLM to the agent
    verbose=True
)

# 3. Create a Task for the Agent
hello_task = Task(
    description='Greet the user with a simple "Hello World!" message.',
    agent=hello_agent,
    expected_output="A simple greeting message"
)

# 4. Create a Crew and Assign the Task
hello_crew = Crew(
    agents=[hello_agent],
    tasks=[hello_task],
    verbose=True
)

# 5. Run the Crew and Get the Result
result = hello_crew.kickoff()

print("\nCrew Result:")
print(result)