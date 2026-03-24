from openai import OpenAI

# Add your Hugging Face API key here
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key="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"
)

def query_huggingface(prompt):
    try:
        completion = client.chat.completions.create(
            model="moonshotai/Kimi-K2-Instruct-0905",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"


# Main program
if __name__ == "__main__":
    user_input = input("Enter your prompt: ")
    
    print("Querying Hugging Face...")
    result = query_huggingface(user_input)
    
    print("Response:")
    print(result)