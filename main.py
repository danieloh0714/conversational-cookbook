import re

from src.recipe import Recipe
from src.utils import is_valid_number


VARIATIONS = {"chinese", "healthy", "unhealthy", "vegan", "vegetarian"}


def get_recipe_url() -> str:
    while True:
        print("Please enter recipe URL:", end=" ")
        recipe_url = input()
        if re.search("allrecipes.com/recipe/[0-9]+/.+", recipe_url):
            return recipe_url
        print("Not a valid recipe URL.")
        recipe_url = ""


def get_servings() -> float:
    while True:
        print("Please enter the number of servings you want:", end=" ")
        servings = input()
        if is_valid_number(servings):
            return float(servings)
        print("Not a valid number.")
        servings = ""


def get_variation_request() -> bool:
    while True:
        print("Would you like a recipe variation? (y/n):", end=" ")
        variation = input().lower()
        if variation == "n":
            return False
        if variation == "y":
            return True
        print("Please enter y/n.")
        variation = ""


def get_variation() -> str:
    print(f"We offer several recipe variations: {VARIATIONS}")
    while True:
        print("Please enter your desired variation:", end=" ")
        variation = input().lower()
        if variation in VARIATIONS:
            return variation
        print("Not a valid variation.")
        variation = ""


def main() -> None:
    recipe_url = get_recipe_url()
    servings = get_servings()
    recipe = Recipe(recipe_url=recipe_url, servings=servings)
    print(f"\n{recipe}")
    print("\n")

    while True:
        variation_request = get_variation_request()
        print("\n")
        if not variation_request:
            print("Have a great day!")
            return

        variation = get_variation()
        print(f"You have selected {variation}")
        print("\n")

        print(f"Here is your {variation} recipe!")
        recipe_variation = Recipe(
            recipe_url=recipe_url, servings=servings, variation=variation
        )
        print(f"\n{recipe_variation}")
        print("\n")


if __name__ == "__main__":
    main()
