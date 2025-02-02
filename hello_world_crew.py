from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama
import os

# --- WORKAROUND (Potentially Required) ---
# The following workaround might still be needed if 
# your CrewAI installation is using an older version
# of the `crewai.cli.constants` file.

from crewai.cli.constants import ENV_VARS

# Override the key name dynamically
for entry in ENV_VARS.get("ollama", []):
    if "API_BASE" in entry:
        entry["BASE_URL"] = entry.pop("API_BASE")
# --- END WORKAROUND ---

# Define your Ollama LLM
ollama_llm = Ollama(
    base_url="http://10.1.1.47:11434",  # Your Ollama server's URL
    model="ollama/qwen2:1.5b",  # Ensure the ollama/ prefix
    verbose=True  # Enable verbose output for debugging
)

# Set the model in environment variable as well, this helps sometimes
os.environ["OLLAMA_MODEL_NAME"] = "ollama/qwen2:1.5b"

# Create a simple agent
agent = Agent(
    role="Tester",
    goal="Test the connection to the Ollama server",
    backstory="An AI agent designed to verify connectivity.",
    llm=ollama_llm,
    verbose=True,
)

# Create a simple task
task = Task(
    description="Say 'Hello, World!'",
    agent=agent,
)

# Instantiate your crew
crew = Crew(
    agents=[agent],
    tasks=[task],
    process=Process.sequential,
    verbose=2,
)

# Run the crew
result = crew.kickoff()

print("######################")
print("Crew Result:")
print(result)