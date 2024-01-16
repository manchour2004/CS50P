# Converts text to emoji
def main():
    text = input("Text: ").replace("_", "")  # Prompts user for text and removes dashes
    emoji_list = {":1stplacemedal:": "🥇", ":moneybag:": "💰", ":candy:": "🍬"}  # Dict containing text mapped to an emoji
    # Condition checks if text is in emoji
    if text in emoji_list:
        print(emoji_list[text])  # Prints out the emoji


main()