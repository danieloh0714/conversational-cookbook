import requests
from bs4 import BeautifulSoup


class Recipe:

    def __init__(self, recipe_url: str):
        self.title = ''
        self.overview = dict()
        self.ingredients = []
        self.instructions = dict()
        self.parse_recipe_url(recipe_url)

    def parse_recipe_url(self, recipe_url: str) -> None:
        req = requests.get(recipe_url)
        soup = BeautifulSoup(req.content, 'html.parser')

        title = soup.find('h1', class_='headline').getText()
        self.title = title

        overview_divs = soup.find_all('div', class_='recipe-meta-item-header')
        overview = {el.getText()[:-1]: el.next_sibling.next_sibling.getText()[:-1] for el in overview_divs}
        self.overview = overview

        ingredient_divs = soup.find_all('span', class_='ingredients-item-name')
        ingredients = [el.getText() for el in ingredient_divs]
        self.ingredients = ingredients

        instructions_divs = soup.find('ul', class_='instructions-section').find_all('p')
        instructions = {i+1: el.getText() for i, el in enumerate(instructions_divs)}
        self.instructions = instructions

    def __str__(self) -> str:
        title = f'--- Recipe ---\n{self.title}'

        overview = '--- Overview ---'
        for k, v in self.overview.items():
            overview += f'\n{k}: {v}'

        ingredients = '--- Ingredients ---'
        for ingredient in self.ingredients:
            ingredients += f'\n- {ingredient}'

        instructions = '--- Instructions ---'
        for step, instruction in self.instructions.items():
            instructions += f'\n{step}. {instruction}'

        return f'{title}\n\n{overview}\n\n{ingredients}\n\n{instructions}'
