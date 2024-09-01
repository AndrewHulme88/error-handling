# Define a custom exception
class CustomValueError(ValueError):
    pass

def divide_numbers(a, b):
    try:
        # Attempt to perform the operation that might raise an exception
        result = a / b
    except ZeroDivisionError:
        # Handle specific error: division by zero
        print("Error: Division by zero is not allowed!")
        return None
    except TypeError:
        # Handle type mismatch (e.g., trying to divide a string by an integer)
        print("Error: Both inputs must be numbers!")
        return None
    else:
        # This block runs if no exception was raised in try
        return result
    finally:
        # This block runs regardless of whether an exception was thrown
        print("Division operation completed (or attempted).")

def get_user_input():
    try:
        num = int(input("Enter a number: "))
        # Raise a custom exception if the input is negative
        if num < 0:
            raise CustomValueError("Number must be positive")
    except ValueError as e:
        # Catch ValueError for incorrect inputs like strings
        print(f"Invalid input: {e}")
    except CustomValueError as e:
        # Catch our custom exception
        print(e)
    else:
        return num

# Example usage
dividend = get_user_input()
divisor = get_user_input()

# Only attempt division if we have valid inputs
if dividend is not None and divisor is not None:
    result = divide_numbers(dividend, divisor)
    if result is not None:
        print(f"The result of division is: {result}")
