import requests
from bs4 import BeautifulSoup

from .ingredient_transform import (
    to_chinese,
    to_chinese_utensils,
    to_healthy,
    to_unhealthy,
    to_vegan,
    to_vegetarian,
)
from .utils import scale_numbers


class Recipe:
    def __init__(self, recipe_url: str, servings: float, variation: str = ""):
        self.title = ""
        self.overview = dict()
        self.ingredients = []
        self.instructions = dict()
        self.servings = servings
        self.variation = variation
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

        self.title = self.__transform(soup.find("h1", class_="headline").getText())

        overview_divs = soup.find_all("div", class_="recipe-meta-item-header")
        for el in overview_divs:
            key = el.getText()[:-1].lower()
            val = el.next_sibling.next_sibling.getText()[:-1]
            if "serving" in key or "yield" in key:
                val = scale_numbers(val, self.servings)
            self.overview[key] = self.__transform(val)

        ingredient_divs = soup.find_all("span", class_="ingredients-item-name")
        self.ingredients = [
            self.__transform(scale_numbers(el.getText(), self.servings))
            for el in ingredient_divs
        ]

        instructions_divs = soup.find("ul", class_="instructions-section").find_all("p")
        self.instructions = {
            i + 1: self.__transform(el.getText())
            for i, el in enumerate(instructions_divs)
        }

    def __transform(self, line: str) -> str:
        ans = []
        for word in line.lower().split(" "):
            match self.variation:
                case "chinese":
                    if word in to_chinese:
                        ans.append(to_chinese[word])
                    else:
                        ans.append(to_chinese_utensils.get(word, word))
                case "healthy":
                    ans.append(to_healthy.get(word, word))
                case "unhealthy":
                    ans.append(to_unhealthy.get(word, word))
                case "vegan":
                    ans.append(to_vegan.get(word, word))
                case "vegetarian":
                    ans.append(to_vegetarian.get(word, word))
                case _:
                    ans.append(word)

        return " ".join(ans)
