# 1. API CONFIGURATION

from groq import Groq

API_KEY = "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"

client = Groq(api_key=API_KEY)

# 2. QUERY FUNCTION

def query_ai(prompt):

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"

# 3. MAIN EXECUTION

if __name__ == "__main__":

    prompt = input("Enter your prompt: ")

    result = query_ai(prompt)

    print("\nAI Response:\n")
    print(result)