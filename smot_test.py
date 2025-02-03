import smolagents as sa

# Your Ollama server details
base_url = "http://10.1.1.47:11434"
model = "qwen2.5:1.5b"

# Create a ChatAgent to interact with the LLM
agent = sa.ChatAgent(
    base_url=base_url,
    model=model,
)

# Define a simple prompt
user_message = "Say 'Hello, world!'"

# Send the prompt to the agent and get the response
response = agent.chat(user_message)

# Print the response
print(response)