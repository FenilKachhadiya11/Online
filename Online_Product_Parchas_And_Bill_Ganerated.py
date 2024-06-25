# Dictionary containing item prices
prices = {
    "tea": 10,
    "coffee": 20,
    "milk": 10,
    "butter": 10,
    "leptop":20000,
    "phone":20000
}

# Initialize an empty list to store user's choices
user_choices = []

# Function to calculate total bill
def calculate_bill(choices):
    total = 0
    for item in choices:
        if item in prices:
            total += prices[item]
    return total

# Function to display menu and get user input
def display_menu():
    print("Welcome to the store!")
    print("Here are the available items and their prices:")
    for item, price in prices.items():
        print(f"{item}: ${price}")

# Main program loop
while True:
    display_menu()
    
    # Ask user to choose an item
    choice = input("Enter item name (or 'done' to finish): ").strip().lower()
    
    # Check if user wants to finish
    if choice == "done":
        break
    
    # Check if the item exists in the prices dictionary
    if choice in prices:
        user_choices.append(choice)
    else:
        print("Invalid choice! Please choose an item from the menu.")
    
    print()  # Blank line for readability

# Calculate and display the total bill
total_bill = calculate_bill(user_choices)
print(f"Your total bill is: ${total_bill}")

print("Thank you for shopping with us!")

