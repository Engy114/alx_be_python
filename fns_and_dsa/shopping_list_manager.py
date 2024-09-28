# shopping_list_manager.py

# Display the menu options
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# Main function to implement the shopping list management
def main():
    shopping_list = []  # Initialize an empty list for shopping items
    
    while True:
        display_menu()  # Display the menu to the user
        choice = input("Enter your choice: ")

        # Handle the user's choice
        if choice == '1':
            # Prompt for item name and add it to the list
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to the shopping list.")

        elif choice == '2':
            # Prompt for item name and try to remove it from the list
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")

        elif choice == '3':
            # Display the shopping list
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")

        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break

        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")

# Check if this script is the main module
if __name__ == "__main__":
    main()
 
