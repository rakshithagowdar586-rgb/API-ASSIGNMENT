import cohere

# 👉 Put your API key here
co = cohere.Client("2DwMGTP4JpyoHaOhMG8GH0pGDEv8VCesZJ4DHWzb")

def chat():
    try:
        user_input = input("Enter your prompt: ")

        response = co.chat(
            message=user_input
        )

        print("\nResponse:")
        print(response.text)

    except Exception as e:
        print("Error:", e)


chat()