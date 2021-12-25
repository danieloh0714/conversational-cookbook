import re

from src.recipe import Recipe
from src.utils import is_valid_number


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


def main() -> None:
    recipe_url = get_recipe_url()
    servings = get_servings()
    recipe = Recipe(recipe_url=recipe_url, servings=servings)
    print(f"\n{recipe}")


if __name__ == "__main__":
    main()
