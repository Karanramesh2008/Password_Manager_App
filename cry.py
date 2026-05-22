from cryptography.fernet import Fernet
import base64
import hashlib

def hash_master(masterpassword: str)->str:
    return hashlib.sha256(masterpassword.encode()).hexdigest()

def derive_mas(masterpassword: str)->str:
    d=hashlib.pbkdf2_hmac('sha256',masterpassword.encode(),b'salt',100000)
    return base64.urlsafe_b64encode(d)

def encrypt(text:str,masterpassword: str)->str:
    d=Fernet(derive_mas(masterpassword))
    return d.encrypt(text.encode()).decode()

def decrypt(ciper_text:str,masterpassword:str)->str:
    d=Fernet(derive_mas(masterpassword))
    return (d.decrypt(ciper_text)).decode()
