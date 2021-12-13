import requests
from bs4 import BeautifulSoup


def parse_recipe_url(url: str):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

    ingredient_divs = soup.find_all('span', class_='ingredients-item-name')
    ingredients = [ingredient.getText() for ingredient in ingredient_divs]
    print(f'Ingredients: {ingredients}')

    instructions_divs = soup.find('ul', class_='instructions-section').find_all('p')
    instructions = [instruction.getText() for instruction in instructions_divs]
    print(f'Instructions: {instructions}')
