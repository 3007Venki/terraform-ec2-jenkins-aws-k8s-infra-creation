# Import necessary modules
import math

# Define a function for addition
def add(x, y):
    return x + y

# Define a function for subtraction
def subtract(x, y):
    return x - y

# Define a function for multiplication
def multiply(x, y):
    return x * y

# Define a function for division
def divide(x, y):
    # Check for division by zero
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

# Define a function for calculating square root
def square_root(x):
    # Check for negative input
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(x)

# Main function to perform calculations
def main():
    # Example calculations
    result_addition = add(5, 3)
    result_subtraction = subtract(5, 3)
    result_multiplication = multiply(5, 3)
    result_division = divide(6, 2)
    result_square_root = square_root(25)

    # Print results
    print("Addition:", result_addition)
    print("Subtraction:", result_subtraction)
    print("Multiplication:", result_multiplication)
    print("Division:", result_division)
    print("Square Root:", result_square_root)

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
