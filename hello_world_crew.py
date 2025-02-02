from crewai import Agent, Task, Crew, Process
from langchain_ollama import ChatOllama  # Updated import

# Define your Ollama LLM
ollama_llm = ChatOllama(
    base_url="http://10.1.1.47:11434",  # Ollama server URL
    model="qwen2.5:1.5b",                 # Model name WITHOUT 'ollama/' prefix
    temperature=0.3                     # Recommended for better control
)

# Create agent and task
agent = Agent(
    role="Tester",
    goal="Test Ollama connection",
    backstory="AI agent verifying connectivity",
    llm=ollama_llm,
    verbose=True
)

task = Task(
    description="Say 'Hello, World!'",
    agent=agent,
    expected_output="The phrase 'Hello, World!' as a simple greeting."
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    process=Process.sequential,
    verbose=True
)

# Run the crew
result = crew.kickoff()
print("\n######################\nCrew Result:\n", result)