from crewai import Agent, Task, Crew, Process
#from langchain_community.chat_models import ChatOllama
from langchain_community.llms import Ollama
import os

# --- WORKAROUND (Potentially Required) ---
# Only needed if you set OLLAMA_BASE_URL in your environment
# and are not passing it directly to the ChatOllama constructor.
from crewai.cli.constants import ENV_VARS

# Override the key name dynamically
for entry in ENV_VARS.get("ollama", []):
    if "API_BASE" in entry:
        entry["BASE_URL"] = entry.pop("API_BASE")
# --- END WORKAROUND ---

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
    verbose=2,
)

# Create a simple task with expected_output
task = Task(
    description="Say 'Hello, World!'",
    agent=agent,
    expected_output="The phrase 'Hello, World!' as a simple greeting.",
)

# Instantiate your crew with verbose=True (for boolean True/False)
crew = Crew(
    agents=[agent],
    tasks=[task],
    process=Process.sequential,
    verbose=2,  # 0, 1, or 2 for different levels of verbosity
)

# Run the crew
result = crew.kickoff()

print("######################")
print("Crew Result:")
print(result)