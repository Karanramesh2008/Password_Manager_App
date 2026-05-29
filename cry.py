import hashlib
import base64
from cryptography.fernet import Fernet
 
def hash_master(masterpassword: str) -> str:
    return hashlib.sha256(masterpassword.encode()).hexdigest()
 
def derive_mas(masterpassword: str) -> bytes:
    key = hashlib.pbkdf2_hmac('sha256', masterpassword.encode(), b'salt', 100000)
    return base64.urlsafe_b64encode(key)
 
def encrypt(text: str, masterpassword: str) -> str:
    d = Fernet(derive_mas(masterpassword))
    return d.encrypt(text.encode()).decode()
 
def decrypt(cipher_text: str, masterpassword: str) -> str:
    d = Fernet(derive_mas(masterpassword))
    return (d.decrypt(cipher_text)).decode()