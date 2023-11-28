import math

def add(x, y):
    """Function to perform addition."""
    return x + y

def subtract(x, y):
    """Function to perform subtraction."""
    return x - y

def multiply(x, y):
    """Function to perform multiplication."""
    return x * y

def divide(x, y):
    """Function to perform division."""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def square_root(x):
    """Function to calculate square root."""
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(x)

def main():
    """Main function to perform calculations."""
    # Example calculations
    result_addition = add(5, 3)
    result_subtraction = subtract(5, 3)
    result_multiplication = multiply(5, 3)
    
    # Handle division exception
    try:
        result_division = divide(6, 0)
        print("Division:", result_division)
    except ValueError as ve:
        print(ve)

    result_square_root = square_root(25)

    # Print results
    print("Addition:", result_addition)
    print("Subtraction:", result_subtraction)
    print("Multiplication:", result_multiplication)
    print("Square Root:", result_square_root)

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
