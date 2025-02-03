#!/usr/bin/env python3
import requests
import json

def main():
    # URL for the Ollama model endpoint.
    # For model "qwen2.5:1.5b", we call the "/generate" endpoint.
    url = "http://10.1.1.47:11434/api/models/qwen2.5:1.5b/generate"
    
    # The headers and payload to send.
    headers = {"Content-Type": "application/json"}
    payload = {
        "prompt": "Hello world"
    }
    
    try:
        # Send the POST request to the server.
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
    except requests.RequestException as e:
        print("Error connecting to the Ollama server:", e)
        return

    try:
        # Parse the JSON response.
        result = response.json()
    except ValueError as e:
        print("Error parsing JSON response:", e)
        return

    # Print the server's response in a pretty JSON format.
    print("Response from Ollama server:")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
