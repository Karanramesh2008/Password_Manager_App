import cry
import auth
import database as db
import generator
import utils

def add_password(master:str):
    site=input("Enter the Site Name: ")
    user=input("Enter the Username: ")
    password=generator.get_user_choice()
    e=cry.encrypt(password,master)
    db.add_password(site,user,e)
    print("Password Successfully Saved.")

def view_password(master:str):
    s=db.get_all_password()
    print(f"{'ID':<10} |{'site':<12}| {'Username':<30}| {'Passwords':>15}")
    for a in s:
            print(f"{a[0]:<10} |{a[1]:<12}| {a[2]:<30}| {cry.decrypt(a[3],master):>15}")
    return

def search_password(master: str):
    site=input("Enter the site name to Search: ")
    s=db.search_password(site)
    print(f"{'ID':<10} |{'site':<12}| {'Username':<30}| {'Passwords':>15}")
    for a in s:
            print(f"{a[0]:<10} |{a[1]:<12}| {a[2]:<30}| {cry.decrypt(a[3],master):>15}")
    return

def delete_password(master: str):
    site=input("Enter the site name to Delete: ")
    db.delete_password(site)

def copy_password(master: str):
    site=input("Enter the site name to Copy: ")
    s=db.search_password(site)
    if not s:
        print("No Password Available")
        return
    if len(s)==1:
        dec=cry.decrypt(s[0][3],master)
        utils.copy_to_clipboard(dec)
        return
    
    utils.display_password(s,master)
    a=int(input("Enter ID to copy: "))
    for x in s:
        if x[0]==a:
            de=cry.decrypt(x[3],master)
            utils.copy_to_clipboard(de)
            return
    print("Invalid ID")
    

def main():
    db.createdb()
    if not db.is_master_set():
        auth.setup_master()
    master=auth.verify_master()

    while True:
        print("\n Password Manager.")
        print("1. Add Password")
        print("2. View All Password")
        print("3. Search Password by Site Name")
        print("4. Delete Password")
        print("5. Copy Password to Clipboard")
        print("6.Quit")
        try:
            ch=int(input("Enter your Choice: "))
            if ch==1:
               add_password(master)
            elif ch==2:
                view_password(master)
            elif ch==3:
                search_password(master)
            elif ch==4:
                delete_password(master)
            elif ch==5:
                 copy_password(master)
            elif ch==6:
                print("Thank you for using our App")
                break
            else:
                print("Invalid Choice.")
        except ValueError:
            print("Invalid Choice.")

if __name__=='__main__':
    main()