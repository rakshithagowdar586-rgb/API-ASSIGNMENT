import requests

url = "http://localhost:11434/api/generate"

def query_ollama(prompt):
    try:
        payload = {
            "model": "phi3",   # use smaller model
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(url, json=payload)

        return response.json()["response"]

    except Exception as e:
        return f"Error: {e}"

prompt = input("Enter your prompt: ")

result = query_ollama(prompt)

print("\nAI Response:\n")
print(result)