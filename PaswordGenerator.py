import random
import string
import time

def generate_password(length=12):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    password_chars = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    if length > 4:
        all_chars = lower + upper + digits + symbols
        password_chars += random.choices(all_chars, k=length - 4)

    random.shuffle(password_chars)
    return ''.join(password_chars)

def main():
    answer = input("Do you want to generate a password? (Yes/No): ").strip().lower()

    if answer == "yes":
        print("Password is being generated...")
        time.sleep(1)
        pwd = generate_password()
        print("Generated password:", pwd)

        # Parolayı dosyaya yazalım
        with open("password.txt", "w") as f:
            f.write(pwd)

        print("Password has been saved to 'password.txt' file.")
    elif answer == "no":
        print("Okay, exiting the program.")
    else:
        print("Invalid input. Please enter Yes or No.")

if __name__ == "__main__":
    main()
