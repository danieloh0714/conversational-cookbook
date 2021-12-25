import requests
from bs4 import BeautifulSoup

from .utils import scale_numbers


class Recipe:
    def __init__(self, recipe_url: str, servings: float):
        self.title = ""
        self.overview = dict()
        self.ingredients = []
        self.instructions = dict()
        self.servings = servings
        self.parse_recipe_url(recipe_url)

    def __str__(self) -> str:
        title = f"--- Recipe ---\n{self.title}"

        overview = "--- Overview ---"
        for k, v in self.overview.items():
            overview += f"\n{k}: {v}"

        ingredients = "--- Ingredients ---"
        for ingredient in self.ingredients:
            ingredients += f"\n- {ingredient}"

        instructions = "--- Instructions ---"
        for step, instruction in self.instructions.items():
            instructions += f"\n{step}. {instruction}"

        return f"{title}\n\n{overview}\n\n{ingredients}\n\n{instructions}"

    def parse_recipe_url(self, recipe_url: str) -> None:
        req = requests.get(recipe_url)
        soup = BeautifulSoup(req.content, "html.parser")

        self.title = soup.find("h1", class_="headline").getText()

        overview_divs = soup.find_all("div", class_="recipe-meta-item-header")
        for el in overview_divs:
            key = el.getText()[:-1].lower()
            val = el.next_sibling.next_sibling.getText()[:-1]
            if "serving" in key or "yield" in key:
                val = scale_numbers(val, self.servings)
            self.overview[key] = val

        ingredient_divs = soup.find_all("span", class_="ingredients-item-name")
        self.ingredients = [
            scale_numbers(el.getText(), self.servings) for el in ingredient_divs
        ]

        instructions_divs = soup.find("ul", class_="instructions-section").find_all("p")
        self.instructions = {
            i + 1: el.getText() for i, el in enumerate(instructions_divs)
        }
