# Define custom exceptions
class CustomValueError(ValueError):
    pass

class CustomOperationError(ValueError):
    pass

def get_valid_input(prompt, validator, error_message):
    while True:
        try:
            value = input(prompt)
            if not validator(value):
                raise CustomValueError(error_message)
            return int(value)
        except ValueError:
            print("Invalid input. Please enter a number.")
        except CustomValueError as e:
            print(e)

def divide_numbers():
    dividend = get_valid_input("Enter the dividend: ", lambda x: True, "Invalid input")
    divisor = get_valid_input("Enter the divisor: ", lambda x: x != "0", "Cannot divide by zero")

    try:
        result = dividend / divisor
    except TypeError:
        print("Both inputs must be numbers!")
    else:
        print(f"The result of division is: {result}")

def perform_addition():
    num1 = get_valid_input("Enter the first number: ", lambda x: True, "Invalid input")
    num2 = get_valid_input("Enter the second number: ", lambda x: True, "Invalid input")

    try:
        result = num1 + num2
    except TypeError:
        print("Addition requires numeric values.")
    else:
        print(f"The sum is: {result}")

def access_list_element():
    my_list = [1, 2, 3]
    index = get_valid_input("Enter an index to access the list: ", lambda x: x.isdigit(), "Index must be a positive integer")

    try:
        element = my_list[index]
    except IndexError:
        print("The index you entered is out of range.")
    else:
        print(f"The element at index {index} is {element}")

def menu():
    while True:
        print("\nError Handling Menu:")
        print("1. Division")
        print("2. Addition")
        print("3. Access List Element")
        print("4. Exit")
        choice = input("Choose an operation: ")

        if choice == "1":
            divide_numbers()
        elif choice == "2":
            perform_addition()
        elif choice == "3":
            access_list_element()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose a number from the menu.")

if __name__ == "__main__":
    menu()
