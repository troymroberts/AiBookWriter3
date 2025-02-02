from crewai import Agent, Crew, Task, Process
from langchain_ollama import ChatOllama

# Define your Ollama LLM
ollama_llm = ChatOllama(
    base_url="http://10.1.1.47:11434",
    model="ollama/qwen2.5:1.5b",
    temperature=0.7
)

# Create a very basic agent
researcher = Agent(
    role="Researcher",
    goal="Answer a simple question",
    backstory="An AI agent designed to answer basic questions.",
    verbose=True,
    allow_delegation=False,
    llm=ollama_llm
)

# Create a simple task
task = Task(
    description="What is the capital of France?",
    agent=researcher,
    expected_output="A clear statement indicating that Paris is the capital of France.",  # Added expected output
    output_parser=None  # Make output parser optional
)

# Create a crew with the agent and task
crew = Crew(
    agents=[researcher],
    tasks=[task],
    process=Process.sequential,
    verbose=True
)

# Run the crew
try:
    result = crew.kickoff()
    print("Crew Result:", result)
except Exception as e:
    print(f"An error occurred: {str(e)}")
    raise  # This will show the full error trace