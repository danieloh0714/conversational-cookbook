import requests
from bs4 import BeautifulSoup


def parse_recipe_url(url: str):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

    recipe = {}

    title = soup.find('h1', class_='headline').getText()
    recipe['title'] = title

    overview_divs = soup.find_all('div', class_='recipe-meta-item-header')
    overview = [f'{div.getText()} {div.next_sibling.next_sibling.getText()}'[:-1] for div in overview_divs]
    recipe['overview'] = overview

    ingredient_divs = soup.find_all('span', class_='ingredients-item-name')
    ingredients = [ingredient.getText() for ingredient in ingredient_divs]
    recipe['ingredients'] = ingredients

    instructions_divs = soup.find('ul', class_='instructions-section').find_all('p')
    instructions = [instruction.getText() for instruction in instructions_divs]
    recipe['instructions'] = instructions

    return recipe
