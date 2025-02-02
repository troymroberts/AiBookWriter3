from crewai import Agent, Task, Crew, Process
from langchain_ollama import OllamaLLM  # Import from langchain-ollama

# Define the Ollama LLM instance
ollama_llm = OllamaLLM(model="qwen2.5:1.5b", base_url="http://10.1.1.47:11434")

# Create a simple agent
agent = Agent(
    role='Test Agent',
    goal='Say hello and confirm connection to Ollama',
    backstory='An agent designed to test connectivity.',
    verbose=True,
    llm=ollama_llm
)

# Create a simple task with expected_output
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
    verbose=2
)

# Run the crew
result = crew.kickoff()

# Print the result
print("Crew Result:")
print(result)