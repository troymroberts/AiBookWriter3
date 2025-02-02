from langchain_ollama import ChatOllama

# Initialize the chat model
llm = ChatOllama(
    base_url="http://10.1.1.47:11434",
    model="qwen2.5:1.5b"
)

# Test it
response = llm.invoke("What is 2+2?")
print(response)