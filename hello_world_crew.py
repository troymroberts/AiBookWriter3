import autogen
from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings import OllamaEmbeddings

# Custom Langchain Models
chat_model = ChatOllama(
    model="qwen2.5:1.5b",  # Replace with your Ollama model
    base_url="http://10.1.1.47:11434",  # Replace with your Ollama base URL
    temperature=0.7,
)

embed_model = OllamaEmbeddings(
    model="qwen2.5:1.5b",  # Replace with your Ollama model
    base_url="http://10.1.1.47:11434",  # Replace with your Ollama base URL
)

# Create an AutoGen LLM config
config_list = [
    {
        "model": "qwen2.5:1.5b",  # Replace with your Ollama model
        "api_key": "None",  # Invalid API key for Ollama
        "base_url": "http://10.1.1.47:11434",  # Replace with your Ollama base URL
        "max_retries": 0,
        "custom_llms": [chat_model],
        "custom_embedding_function": [embed_model],
    }
]

llm_config = {
    "config_list": config_list,
    "cache_seed": 42,
    "temperature": 0.7,
}

# Create user proxy agent, coder, and a test group chat
user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    system_message="A human admin.",
    code_execution_config={
        "last_n_messages": 1,
        "work_dir": "groupchat",
        "use_docker": False,
    },  # Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
)

coder = autogen.AssistantAgent(
    name="Coder",
    llm_config=llm_config,
)

groupchat = autogen.GroupChat(agents=[user_proxy, coder], messages=[], max_round=12)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

# Start the conversation
user_proxy.initiate_chat(manager, message="What is the capital of France?")