import re

from src.recipe import Recipe


def get_recipe_url() -> str:
    while True:
        print("Please enter recipe URL:", end=" ")
        recipe_url = input()
        if re.search("allrecipes.com/recipe/[0-9]+/.+", recipe_url):
            return recipe_url
        print("Not a valid recipe URL.")
        recipe = ""


def main() -> None:
    recipe_url = get_recipe_url()
    recipe = Recipe(recipe_url=recipe_url)
    print(f"\n{recipe}")


if __name__ == "__main__":
    main()
