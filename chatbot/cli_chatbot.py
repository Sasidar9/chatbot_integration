import requests

API_URL = "http://localhost:8000/chat"

print("Recipe Chatbot")
print("Type 'exit' to stop")

while True:
    user_input = input("Enter ingredients (comma separated): ")

    if user_input.lower() == "exit":
        break

    ingredients = [i.strip() for i in user_input.split(",")]

    response = requests.post(
        API_URL,
        json={"ingredients": ingredients}
    )

    print("Response:")
    print(response.json()["response"])
    print("-" * 40)
