from langchain_ollama import OllamaLLM

llm = OllamaLLM(base_url="http://10.1.1.47:11434", model="qwen2.5:1.5b")
print(llm.invoke("What is 2+2?"))