
import random
import string

def generate_strong_password(length=12):
    # Define character sets for each category
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure at least one character from each category
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters),
    ]

    # Fill the rest of the password with random characters
    remaining_length = length - len(password)
    password.extend(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(remaining_length))

    # Shuffle the password characters for additional randomness
    random.shuffle(password)

    return ''.join(password)

def generate_multiple_strong_passwords(count=1, length=12):
    passwords = [generate_strong_password(length) for _ in range(count)]
    return passwords

if __name__ == "__main__":
    try:
        password_length = int(input("Enter the desired password length: "))
        password_count = int(input("Enter the number of passwords to generate: "))
    except ValueError:
        print("Please enter valid numeric values.")
        exit()

    passwords = generate_multiple_strong_passwords(password_count, password_length)

    print("\nGenerated Strong Passwords:")
    for idx, password in enumerate(passwords, start=1):
        print(f"Password {idx}: {password}")
