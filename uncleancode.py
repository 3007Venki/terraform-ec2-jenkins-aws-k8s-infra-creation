import os

def process_user_input(input_data):
    """Process user input and execute a command."""
    # Security Concern: Command Injection
    # Explanation: User input is directly used in a command, making it vulnerable to command injection attacks.
    # Recommendation: Use proper input validation and sanitization or utilize safe APIs to execute commands.

    # Insecure Code:
    os.system("echo " + input_data)

    # Secure Code:
    # subprocess.run(["echo", input_data], check=True)

def authenticate_user(username, password):
    """Authenticate user based on provided username and password."""
    # Security Concern: Hardcoded Credentials
    # Explanation: Storing credentials in code can lead to security risks.
    # Recommendation: Use secure storage mechanisms like environment variables or dedicated credential management systems.

    # Insecure Code:
    if username == "admin" and password == "admin123":
        return True
    else:
        return False

    # Secure Code:
    # Use secure storage mechanisms for credentials.

def main():
    user_input = input("Enter data: ")
    process_user_input(user_input)

    # Example of calling authenticate_user
    # In a real application, you would use a secure authentication mechanism.
    username = input("Enter username: ")
    password = input("Enter password: ")
    if authenticate_user(username, password):
        print("Authentication successful")
    else:
        print("Authentication failed")

if __name__ == "__main__":
    main()
