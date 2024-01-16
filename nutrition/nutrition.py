# Program prompts user for fruit as input and outputs amount of calories
def main():
    food = input("Item: ").lower()  # Prompts user for string input and converts all characters to lowercase

    food_items = [   # List of dictionaries containing name of fruit and it's amount of calories

        {'fruit': 'apple', 'calories': 130},
        {'fruit': 'avocado', 'calories': 50},
        {'fruit': 'banana', 'calories': 110},
        {'fruit': 'cantaloupe', 'calories': 50},
        {'fruit': 'grapefruit', 'calories': 60},
        {'fruit': 'grapes', 'calories': 90},
        {'fruit': 'honeydew melon', 'calories': 50},
        {'fruit': 'kiwifruit', 'calories': 90},
        {'fruit': 'lemon', 'calories': 15},
        {'fruit': 'lime', 'calories': 20},
        {'fruit': 'nectarine', 'calories': 60},
        {'fruit': 'orange', 'calories': 80},
        {'fruit': 'peach', 'calories': 60},
        {'fruit': 'pear', 'calories': 100},
        {'fruit': 'pineapple', 'calories': 50},
        {'fruit': 'plums', 'calories': 70},
        {'fruit': 'strawberries', 'calories': 50},
        {'fruit': 'sweet cherries', 'calories': 100},
        {'fruit': 'tangerine', 'calories': 50},
        {'fruit': 'watermelon', 'calories': 80}
    ]

    for item in food_items:
        # Checks if user input is a fruit name on the list
        if item["fruit"] == food:
            print(item["calories"])  # Prints amount of calories


main()