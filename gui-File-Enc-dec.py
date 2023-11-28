from cryptography.fernet import Fernet
import os
import tkinter as tk
from tkinter import filedialog

class FileEncryptor:
    def __init__(self, master):
        self.master = master
        self.master.title("File Encryption and Decryption Tool")

        self.result_label = tk.Label(self.master, text="", wraplength=300)
        self.result_label.pack(pady=10)

        self.create_buttons()

    def create_buttons(self):
        encrypt_button = tk.Button(self.master, text="Encrypt a File", command=self.encrypt_file)
        encrypt_button.pack(pady=5)

        decrypt_button = tk.Button(self.master, text="Decrypt a File", command=self.decrypt_file)
        decrypt_button.pack(pady=5)

    def generate_key(self):
        return Fernet.generate_key()

    def save_key(self, key, key_file):
        with open(key_file, 'wb') as key_file:
            key_file.write(key)

    def load_key(self, key_file):
        return open(key_file, 'rb').read()

    def encrypt_file(self):
        file_path = self.get_file_path()
        if file_path:
            key = self.load_or_generate_key()
            cipher = Fernet(key)

            with open(file_path, 'rb') as file:
                data = file.read()
            encrypted_data = cipher.encrypt(data)

            with open(file_path + '.encrypted', 'wb') as encrypted_file:
                encrypted_file.write(encrypted_data)

            self.update_status("File encrypted successfully.")

    def decrypt_file(self):
        encrypted_file_path = self.get_file_path()
        if encrypted_file_path and encrypted_file_path.endswith('.encrypted'):
            key = self.load_or_generate_key()
            cipher = Fernet(key)

            with open(encrypted_file_path, 'rb') as encrypted_file:
                encrypted_data = encrypted_file.read()
            decrypted_data = cipher.decrypt(encrypted_data)

            with open(encrypted_file_path[:-10], 'wb') as decrypted_file:
                decrypted_file.write(decrypted_data)

            self.update_status("File decrypted successfully.")
        else:
            self.update_status("Invalid file. Please select a valid encrypted file.")

    def load_or_generate_key(self):
        key_file = 'encryption_key.key'
        if not os.path.exists(key_file):
            key = self.generate_key()
            self.save_key(key, key_file)
            self.update_status(f"Key generated and saved to {key_file}")
        else:
            key = self.load_key(key_file)
        return key

    def update_status(self, message):
        self.result_label.config(text=message)

    def get_file_path(self):
        file_path = filedialog.askopenfilename()
        return file_path

def main():
    root = tk.Tk()
    app = FileEncryptor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
