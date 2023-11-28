# Python pseudocode for a Password Generator

# Step 1: Import necessary libraries/modules
import random
import string

# Step 2: Function to generate a random password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Step 3: Function to get user input for password length
def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length > 0:
                return length
            else:
                print("Password length must be greater than 0. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Step 4: Main function
def main():
    length = get_password_length()
    password = generate_password(length)
    print(f"Generated Password: {password}")

# Step 5: Call the main function
if __name__ == "__main__":
    main()
