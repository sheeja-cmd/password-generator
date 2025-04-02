import random
import string

def generate_password(length=12):
    """Generate a random password with letters, digits, and symbols."""
    if length < 4:
        print("Password length should be at least 4.")
        return None

    characters = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    password += random.sample(characters, length - 4)
    random.shuffle(password)
    password = "".join(password)

    return password  # *Return instead of just printing*

if __name__ == "__main__":
    try:
        password_length = int(input("Enter the password length (min 4): "))
        new_password = generate_password(password_length)
        if new_password:
            print(f"Generated Password: {new_password}")  # *Print output*
    except ValueError:
        print("Please enter a valid number.")