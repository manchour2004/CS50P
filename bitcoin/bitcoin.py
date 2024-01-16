# Program outputs the current price in usd of the amount of BTC user typed in the command line
import requests
import sys


def main():
    try:
        # Checks if argumennt count is 2
        if len(sys.argv) == 2:
            try:
                bitcoin_price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")  # Gets the data from the API
                bitcoin_price_usd = bitcoin_price.json()  # Converts the response to JSON

                # Accesses the price in USD and multiplies with the cmd line argument
                btc = float(bitcoin_price_usd["bpi"]["USD"]["rate_float"]) * float(sys.argv[1])
                print(f"${btc:,.4f}")  # Prints the price

            except requests.RequestException:  # Handles Request exceptions
                sys.exit()
        else:
            sys.exit("Missing command line argument")  # Handles cmd line exceptions for argument count

    except ValueError:
        sys.exit("Command line is not a number")  # Handles invalid cmd line exceptions for invalid cmd line argument


main()