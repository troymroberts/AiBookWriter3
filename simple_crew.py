from crewai import Agent, Crew, Task, Process
from langchain_ollama import Ollama  # Updated import
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Define your Ollama LLM with the correct configuration
ollama_llm = Ollama(
    base_url="http://10.1.1.47:11434",
    model="qwen2.5:1.5b",
    temperature=0.7,
    callbacks=[],  # Add empty callbacks to prevent certain errors
    metadata={},   # Add empty metadata to prevent certain errors
)

# Create a very basic agent
researcher = Agent(
    role="Researcher",
    goal="Answer a simple question",
    backstory="An AI agent designed to answer basic questions.",
    verbose=True,
    allow_delegation=False,  # Disable delegation to prevent potential issues
    llm=ollama_llm,
)

# Create a simple task
task = Task(
    description="What is the capital of France?",
    agent=researcher,
    expected_output="The capital of France is Paris."
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
    # Add additional error handling if needed