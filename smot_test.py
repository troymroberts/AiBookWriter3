import asyncio
import os
from smol_dev.smol_agent import SmolAgent

async def main():
    """
    A simple Smol Agents application to test connectivity to an Ollama server.
    """

    # Configure Ollama server connection for Smol Agents
    # Smol Agents often uses OpenAI-like environment variables for API configuration.
    # We'll set OPENAI_API_BASE to your Ollama server URL.
    os.environ["OPENAI_API_BASE"] = "http://10.1.1.47:11434/v1"  # Point to your Ollama server
    os.environ["OPENAI_API_KEY"] = "ollama"  #  Ollama doesn't require an API key, but Smol Agents might expect it to be set. Use a dummy value.
                                            #  Alternatively, you might need to set OLLAMA_HOST if OPENAI_API_BASE doesn't work directly.
                                            #  Try both if one doesn't work immediately.
    # os.environ["OLLAMA_HOST"] = "http://10.1.1.47:11434"  # Try this if OPENAI_API_BASE doesn't work


    # Initialize the Smol Agent, specifying the model
    agent = SmolAgent(
        model="qwen2.5:1.5b",
    )

    # Define a simple task for the agent - say "Hello World"
    task = "Say 'Hello World'"

    print(f"Sending task to Ollama ({agent.llm_model})...")

    try:
        # Run the agent with the task and get the response
        response = await agent.run(task)

        print("\nOllama Response:")
        print(response)

    except Exception as e:
        print(f"\nError communicating with Ollama server: {e}")
        print("Please check:")
        print("- Is your Ollama server running at http://10.1.1.47:11434?")
        print("- Is the model 'qwen2.5:1.5b' installed in your Ollama server?")
        print("- Is there any network connectivity issue between your machine and the Ollama server?")


if __name__ == "__main__":
    asyncio.run(main())