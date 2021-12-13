from src.parser import parse_recipe_url

def main():
    print('Please enter recipe URL:', end=' ')
    recipe_url = input()
    parse_recipe_url(recipe_url)


if __name__ == '__main__':
    main()
