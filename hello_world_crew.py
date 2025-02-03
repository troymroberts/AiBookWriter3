import os
from crewai import Agent, Task, Crew
from langchain_ollama import OllamaLLM

# 1. Define your Ollama LLM with more explicit model_kwargs
ollama_llm = OllamaLLM(
    model='qwen2.5:1.5b',
    base_url='http://localhost:11434', # Keep base_url for OllamaLLM itself
    model_kwargs={
        'base_url': 'http://localhost:11434', # Keep base_url in model_kwargs too
        'api_base': 'http://localhost:11434', # ADD api_base in model_kwargs
        'model': 'qwen2.5:1.5b',
        'provider': 'ollama'
    }
)

# 2. Create a *minimal* Agent
hello_agent = Agent(
    role='Greeting Agent',
    llm=ollama_llm,  # Assign the Ollama LLM to the agent
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