from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)

def encrypt_file_id(file_id: str) -> str:
    return fernet.encrypt(file_id.encode()).decode()

def decrypt_token(token: str) -> str:
    return fernet.decrypt(token.encode()).decode()