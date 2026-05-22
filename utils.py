import pyperclip
import cry

def copy_to_clipboard(text: str):
    pyperclip.copy(text)
    print("Copied to Clipboard")

def display_password(passwords:list,master:list):
    if not passwords:
        print("No passwords available.")
        return
    print(f"{'ID':<10} |{'site':<12}| {'Username':<12}| {'Passwords':>15}")
    for a in passwords:
        print(f"{a[0]:<10} |{a[1]:<12}| {a[2]:>12}| {cry.decrypt(a[3],master):>15}")

