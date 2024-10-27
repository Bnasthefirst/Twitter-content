import secrets
random_bytes = secrets.token_bytes(16)  # Generates 16 random bytes

token = secrets.token_hex(16)  
# Generates a 32-character hexadecimal token


url_safe_token = secrets.token_urlsafe(16)  # URL-safe token


choices = ['apple', 'banana', 'cherry']
secure_choice = secrets.choice(choices)  # Randomly selects an item from the list


import secrets
import string

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

secure_password = generate_password()
print(secure_password)
