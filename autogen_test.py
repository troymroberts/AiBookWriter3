from autogen import AssistantAgent, UserProxyAgent


config_list = [
    {
        "model": "qwen:2.5:1b",
        "base_url": "http://10.1.1.47:11434/v1",  # Your Ollama server address
        "api_key": "ollama",  # Placeholder, as Ollama doesn't require a key by default
    }
]

llm_config = {
    "config_list": config_list,
}

# Create an AssistantAgent named "assistant"
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config,
)

# Create a UserProxyAgent named "user_proxy"
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=1,  # Adjust as needed for longer conversations
    code_execution_config=False,  # Disable code execution for this simple test
    llm_config=llm_config,
    system_message="Reply TERMINATE if the task has been solved at full satisfaction.",
)

# Start the conversation
user_proxy.initiate_chat(
    assistant,
    message="""
        What is the date today?
        Please reply with the date and say hello world.
    """,
)