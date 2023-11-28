from flask import Flask, render_template, request
from cryptography.fernet import Fernet
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt_file():
    key = load_or_generate_key()
    cipher = Fernet(key)

    file = request.files['file']
    data = file.read()
    encrypted_data = cipher.encrypt(data)

    with open(f"uploads/{file.filename}.encrypted", 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    return "File encrypted successfully."

@app.route('/decrypt', methods=['POST'])
def decrypt_file():
    key = load_or_generate_key()
    cipher = Fernet(key)

    file = request.files['file']
    encrypted_data = file.read()
    decrypted_data = cipher.decrypt(encrypted_data)

    with open(f"uploads/{file.filename[:-10]}", 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    return "File decrypted successfully."

def load_or_generate_key():
    key_file = 'encryption_key.key'
    if not os.path.exists(key_file):
        key = generate_key()
        save_key(key, key_file)
    else:
        key = load_key(key_file)
    return key

def generate_key():
    return Fernet.generate_key()

def save_key(key, key_file):
    with open(key_file, 'wb') as key_file:
        key_file.write(key)

def load_key(key_file):
    return open(key_file, 'rb').read()

if __name__ == '__main__':
    app.run(debug=True)
