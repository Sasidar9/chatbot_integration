from fastapi import FastAPI
from pydantic import BaseModel
import json
from llm import generate_recipe

app = FastAPI()

with open("../data/recipes.json", "r") as file:
    recipes = json.load(file)

class IngredientInput(BaseModel):
    ingredients: list[str]

@app.post("/chat")
def chat(input_data: IngredientInput):
    response = generate_recipe(input_data.ingredients, recipes)
    return {
        "ingredients": input_data.ingredients,
        "response": response
    }
