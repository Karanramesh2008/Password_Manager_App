import random
import string

def generate_password(length: int=16)->str:
    s=string.ascii_letters+string.digits+string.punctuation
    re=random.choices(s,k=length)
    return "".join(re)

def get_user_choice():
    i=input("Do you want to generate password or own: ")
    if i=='own':
        d=input("Enter your Password: ")
        return d
    else:
        f=int(input("Enter the length of the password: "))
        return generate_password(f)
