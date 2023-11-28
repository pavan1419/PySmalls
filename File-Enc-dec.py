# Python pseudocode for a File Encryption and Decryption tool

# Step 1: Import necessary libraries/modules
from cryptography.fernet import Fernet
import os

# Step 2: Function to generate a key for encryption/decryption
def generate_key():
    return Fernet.generate_key()

# Step 3: Function to save the key to a file
def save_key(key, key_file):
    with open(key_file, 'wb') as key_file:
        key_file.write(key)

# Step 4: Function to load the key from a file
def load_key(key_file):
    return open(key_file, 'rb').read()

# Step 5: Function to encrypt a file
def encrypt_file(file_path, key):
    cipher = Fernet(key)
    with open(file_path, 'rb') as file:
        data = file.read()
    encrypted_data = cipher.encrypt(data)
    with open(file_path + '.encrypted', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
    print("File encrypted successfully.")

# Step 6: Function to decrypt a file
def decrypt_file(encrypted_file_path, key):
    cipher = Fernet(key)
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    with open(encrypted_file_path[:-10], 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)
    print("File decrypted successfully.")

# Step 7: Function to display the encryption key
def display_key(key):
    print(f"Encryption Key: {key.decode()}")

# Step 8: Function to find all encrypted files in a folder
def find_encrypted_files(folder_path):
    encrypted_files = [file for file in os.listdir(folder_path) if file.endswith('.encrypted')]
    if encrypted_files:
        print("Encrypted files found:")
        for file in encrypted_files:
            print(file)
    else:
        print("No encrypted files found in the folder.")

# Step 9: Main function
def main():
    key_file = 'encryption_key.key'

    # Check if the key exists, generate one if not
    if not os.path.exists(key_file):
        key = generate_key()
        save_key(key, key_file)
        print(f"Key generated and saved to {key_file}")
    else:
        key = load_key(key_file)

    choice = input("Enter 'E' to encrypt a file, 'D' to decrypt a file, 'S' to show the key, or 'F' to find encrypted files in a folder: ").upper()

    if choice == 'E':
        file_path = input("Enter the path of the file to encrypt: ")
        encrypt_file(file_path, key)
    elif choice == 'D':
        encrypted_file_path = input("Enter the path of the encrypted file: ")
        decrypt_file(encrypted_file_path, key)
    elif choice == 'S':
        display_key(key)
    elif choice == 'F':
        folder_path = input("Enter the path of the folder to search for encrypted files: ")
        find_encrypted_files(folder_path)
    else:
        print("Invalid choice. Please enter 'E', 'D', 'S', or 'F'.")

# Step 10: Call the main function
if __name__ == "__main__":
    main()
