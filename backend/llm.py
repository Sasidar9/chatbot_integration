import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_recipe(user_ingredients, recipes):
    user_ingredients = [i.lower() for i in user_ingredients]

    for item in recipes:
        if all(ing in user_ingredients for ing in item["ingredients"]):
            return f"Recipe: {item['recipe']}\nSteps: {item['steps']}"

    prompt = (
        "Suggest a simple cooking recipe using these ingredients: "
        + ", ".join(user_ingredients)
    )

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "phi",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]
