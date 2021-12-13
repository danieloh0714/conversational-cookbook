from src.parser import Recipe


def main():
    print('Please enter recipe URL:', end=' ')
    recipe_url = input()
    recipe = Recipe(recipe_url=recipe_url)
    print(recipe)


if __name__ == '__main__':
    main()
