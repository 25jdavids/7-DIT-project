food_menu = {
    "Classic burger with fries": 28.50,
    "Portugal burger with fries": 33.50,
    "American classic": 25.40,
    "Spaghetti bolognaise": 36.87,
    "Margherita pizza": 31.72,
    "Classic pizza": 27.00,
    "Meaty pizza": 40.00,
    "Salad": 15.52,
    "Veggie pizza": 28.09
}

drinks_menu = {
    "Coke/Coke Zero": 9.00,
    "Sprite/Sprite Zero": 9.00,
    "Fruit juice": 12.00,
    "Milkshake special": 17.00,
    "Coffee": 15.00,
    "Tea": 15.00,
    "Beer": 24.00,
    "Wine (Red/White)": 27.00
}

final_order = {}  # Stores the finalized items ordered

def show_menu(menu, menu_type):
    """Function to display the menu."""
    print(f"\n{menu_type} Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")

def customer_details():
    """Function to take customer details."""
    name = input('Enter the customer\'s name: ')
    address = input('Enter the customer\'s address: ')
    phone = input('Enter the customer\'s phone number: ')
    print("Customer details saved.\n")

def add_order():
    """Function to add items to the order."""
    while True:
        item = input("Enter the item to add (or type 'done' to finish): ")
        if item == 'done':
            break
        if item in food_menu or item in drinks_menu:
            quantity = int(input(f"Enter quantity for {item}: "))
            final_order[item] = final_order.get(item, 0) + quantity
            print(f"Added {quantity}x {item} to the order.")
        else:
            print("Item not found in the menu. Please try again.")

def calculate_total():
    """Function to calculate and display the total cost of the order."""
    if not final_order:
        print("\nNo items in the order yet.")
        return

    subtotal = sum((food_menu.get(item, 0) + drinks_menu.get(item, 0)) * quantity for item, quantity in final_order.items())

    delivery = input("Is this order for delivery? (yes/no): ").lower
    delivery_fee = 8.00 if delivery == "yes" else 0.00
    total = subtotal + delivery_fee

    print(f"\nSubtotal: ${subtotal:.2f}")
    if delivery_fee:
        print(f"Delivery Fee: ${delivery_fee:.2f}")
    print(f"Total Amount Due: ${total:.2f}")

def summary_order(menu_type):
    """Function to display the summary of the customer's order based on menu type."""
    if not final_order:
        print("\nNo items in the order yet.")
        return
    print("\nOrder Summary:")
    subtotal = 0
    for item, quantity in final_order.items():
        if menu_type == "food" and item not in food_menu:
            continue
        if menu_type == "drinks" and item not in drinks_menu:
            continue
        price = food_menu.get(item, drinks_menu.get(item, 0))
        item_total = price * quantity
        subtotal += item_total
        print(f"{item} x{quantity} = ${item_total:.2f}")
    print(f"\nSubtotal: ${subtotal:.2f}")

def home():
    """Main menu system."""
    while True:
        print("\nKingp/n Online Order Manager")
        print("1. Show the food menu")
        print("2. Show the drinks menu")
        print("3. Enter customer details")
        print("4. Add items to order")
        print("5. Calculate total cost")
        print("6. View order summary")
        print("7. Exit")

        choice = input("Please select an option from 1 to 7: ")

        if choice == "1":
            show_menu(food_menu, "Food")
        elif choice == "2":
            show_menu(drinks_menu, "Drinks")
        elif choice == "3":
            customer_details()
        elif choice == "4":
            add_order()
        elif choice == "5":
            calculate_total()
        elif choice == "6":
            summary_order()
        elif choice == "7":
            print("Goodbye!!!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__": 
    home()