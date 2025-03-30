food_menu = {"Classic burger with fries": 28.50,  #The menu for all the food that can possibly be ordered
             "Portugal burger with fries": 33.50,
             "American classic": 25.40,
             "Spaghetti bolognaise": 36.87,
             "Marghareita pizza": 31.72,
             "Classic pizza": 27.00,
             "Meaty pizza": 40.00,
             "Slad": 15.52,
             "Veggie pizza": 28.09 
            }
drinks_menu = {"Coke/Coke Zero":9.00,  #Menu for all the drinks that can possibly be ordered 
               "Sprite/Sprite Zero":9.00,
               "Fruit juice":12.00,
               "Milkshake special":17.00,
               "Coffee":15.00,
               "Tea":15.00,
               "Beer":24.00,
               "Wine(Red/White)":27.00
               }

final_order = {} #stores the finalised items ordered from the above lists

def show_menu(menu,menu_type):
    """Function to display the menu"""
    print(f"\n{menu_type} Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")

def customer_details():
    """Function to take the details of the customers which we will later store in the system"""
    names = str(input('Enter the customers name and surname: '))#customers name
    adress = input('enter the customers adress: ')#customers adress
    phonenumber = int(input('Enter the customers phone number: '))#customers phone number
    food = input('Enter the type of food the customer has ordered: ')#type of food customer ordered
    method = input('enter if the food is for pickup or delivery: ')#Type of order for pickup or delivery

def calculate_total():
    """Funtion to calculate the total of the customers order"""
    Amount_Total = sum((food_menu.get(item, 0) + drinks_menu.get(item, 0)) * amount for item, amount in final_order.items())#Calculating the total amount that the order is going to cost
    delivery_fee = 8.00  #Showing the delivery fee
    total = Amount_Total + delivery_fee#Getting the subtotal

def summary_order():
    """Function to get the summary of the customers order"""
    print("\nOrder Summary:")#Printing the summmary of the customers order
    for item, quantity in final_order.items():
        price = food_menu.get(item, drinks_menu.get(item, 0))
        print(f"{item} x{quantity} = ${price * quantity:.2f}")

def main_menu():
    "Function to call the menu system up on my program"
    while True:
        print("\nKingp/n online order manager")#Heading of the menu
        print("1.Show the orders menu")#Option 1 of the menu
        print("2.Enter your personla details")#Option 2 of the menu
        print("3.Calculate the total of your order")#Option 3 of the menu
        print("4.Summarise the customers order")#Option 4 of the menu
        print("5. Exit the program")#Option 6 of the menu to exit the program 
        
        choice = input("Please select an option from 1-6: ")#Asking the user to make a choice
        
        if choice == "1":#displaying the students choice
            show_menu()
        elif choice == "2":#displaying the students choice
            customer_details()
        elif choice == "3":#displaying the students choice
            calculate_total()
        elif choice == "4":#displaying the students choice
            summary_order()
        elif choice == "5":#displaying the students choice
            print("Goodbye!Have a good day")#If the student chooses option 6 the program ends and there is a goodbye message displayed
            break
        else:
            print("You have selected an invalid option, please try again.")#Input validation

if __name__ == "__main__":
    main_menu()







