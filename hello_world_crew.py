from crewai import Agent, Task, Crew
from langchain_community.chat_models import ChatOllama

# 1. Configure Ollama connection
ollama_llm = ChatOllama(
    base_url="http://10.1.1.47:11434",  # Direct URL to your Ollama server
    model="qwen2.5:1.5b",  # Verify exact model name in your Ollama
    temperature=0.7
)

# 2. Create a test agent
hello_agent = Agent(
    role='Test Assistant',
    goal='Respond to simple prompts',
    backstory='You are a connectivity test agent',
    llm=ollama_llm,  # Assign the custom Ollama configuration
    verbose=True
)

# 3. Create a simple task
hello_task = Task(
    description='Say "Hello World"',
    agent=hello_agent
)

# 4. Create and run the crew
test_crew = Crew(
    agents=[hello_agent],
    tasks=[hello_task],
    verbose=2
)

result = test_crew.kickoff()
print("Test Result:", result)