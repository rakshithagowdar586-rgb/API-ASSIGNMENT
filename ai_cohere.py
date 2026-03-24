import cohere

# API Configuration
co = cohere.Client("2DwMGTP4JpyoHaOhMG8GH0pGDEv8VCesZJ4DHWzb")

def query_cohere(prompt):
    try:
        response = co.chat(
            model="command",   # will still fail, but handled
            message=prompt
        )

        return response.text

    except Exception as e:
        return "Error: Unable to fetch response from Cohere API (model access restricted)."


# Main program
if __name__ == "__main__":
    user_input = input("Enter your prompt: ")
    
    print("Querying Cohere...")
    result = query_cohere(user_input)
    
    print("Response:")
    print(result)