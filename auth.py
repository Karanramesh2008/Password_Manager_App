import getpass
import cry
import database as db

def setup_master():
    i=getpass.getpass("Enter the new Master Password: ")
    c=getpass.getpass("Confirm the Password: ")
    if i==c:
        db.save_master_hash(cry.hash_master(i))
    else:
        print("Password not Match!")
        return setup_master()
    

def verify_master():
    i=getpass.getpass("Enter the Master Password: ")
    if cry.hash_master(i)==db.get_master_hash():
        print("Master Password Matched")
        return i
    
    else:
        print("Incorrect Master Password")
        return verify_master()
    