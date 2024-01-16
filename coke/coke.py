# A coke vending machine
def main():
    amount_due = 50  # Price of Coke

    while amount_due != 0:  # Iterates provided that amount_due is not equal to 0
        print(f"Amount Due: {amount_due}")  # Outputs Amount due on each iteration
        coins = int(input("Insert coins: "))  # Prompts user for number of coins

        # Constraint that keeps prompting user for coins
        if not (coins == 25 or coins == 10 or coins == 5):
            continue

        amount_due -= coins  # Amount due decreases by number of coins inserted for each iteration

        # Returns change owed if user inputs more coins than due
        if amount_due < 0:
            amount_due = - (amount_due)
            print(f"Change Owed: {amount_due}")
            break  # exits the loop
    # If Amount due is equal to 0
    else:
        print(f"Change Owed: {amount_due}")


main()