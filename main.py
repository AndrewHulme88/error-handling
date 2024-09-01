# Custom exceptions
class CustomValueError(ValueError):
    pass

class OutOfRangeError(ValueError):
    pass

def menu():
    print("\nError Handling Demonstrations:")
    print("1. Division Operation")
    print("2. Age Validator")
    print("3. File Operation")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")
    return choice

def get_input(prompt, error_type=None, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if error_type == 'age':
                if value < min_val or value > max_val:
                    raise OutOfRangeError(f"Age must be between {min_val} and {max_val}")
            return value
        except ValueError:
            print("Please enter a valid number.")
        except OutOfRangeError as e:
            print(e)

def division_operation():
    try:
        a = get_input("Enter dividend: ")
        b = get_input("Enter divisor: ")
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero! Please try again.")
    else:
        print(f"Result of {a} / {b} = {result}")
    finally:
        print("Division attempt completed.")

def age_validator():
    age = get_input("Enter your age: ", error_type='age', min_val=0, max_val=120)
    if age:
        print(f"Your age, {age}, has been validated.")

def file_operation():
    try:
        # Attempt to open a non-existent file
        with open('non_existent_file.txt', 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print("The file does not exist. Would you like to create it? (y/n)")
        choice = input().lower()
        if choice == 'y':
            with open('non_existent_file.txt', 'w') as file:
                file.write("This file was created due to a FileNotFoundError.")
            print("File has been created.")
        else:
            print("Operation cancelled.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")

def main():
    while True:
        choice = menu()
        if choice == '1':
            division_operation()
        elif choice == '2':
            age_validator()
        elif choice == '3':
            file_operation()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
