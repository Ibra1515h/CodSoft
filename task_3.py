import random
import string

def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length > 0:
                return length
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    password_length = get_password_length()
    password = generate_password(password_length)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()