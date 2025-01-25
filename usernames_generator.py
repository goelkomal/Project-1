import random
import string

# Lists of words to create usernames
adjectives = ["Swift", "Clever", "Brave", "Mighty", "Sly", "Fierce", "Charming", "Witty", "Bold", "Eager"]
nouns = ["Tiger", "Dragon", "Phoenix", "Wolf", "Eagle", "Shark", "Ninja", "Knight", "Wizard", "Viking"]

def generate_username(include_numbers, include_special_chars, length):
    # Start with a random adjective and noun
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    
    # Combine them
    username = f"{adjective}{noun}"
    
    # Add numbers if specified
    if include_numbers:
        username += str(random.randint(1, 99))  # Add a random number between 1 and 99
    
    # Add special characters if specified
    if include_special_chars:
        special_char = random.choice(string.punctuation)
        username += special_char
    
    # Trim or pad the username to the specified length
    if len(username) > length:
        username = username[:length]
    elif len(username) < length:
        username = username.ljust(length, 'x')  # Pad with 'x' if shorter
    
    return username

def generate_multiple_usernames(count, include_numbers, include_special_chars, length):
    usernames = set()  # Use a set to avoid duplicates
    while len(usernames) < count:
        usernames.add(generate_username(include_numbers, include_special_chars, length))
    return list(usernames)

def save_usernames_to_file(usernames, filename="usernames.txt"):
    with open(filename, "w") as file:
        for username in usernames:
            file.write(username + "\n")
    print(f"User names saved to {filename}")

def main():
    print("Welcome to the Username Generator!")
    
    # Get user input for customization
    count = int(input("How many unique usernames would you like to generate? "))
    include_numbers = input("Include numbers in usernames? (yes/no): ").strip().lower() == 'yes'
    include_special_chars = input("Include special characters in usernames? (yes/no): ").strip().lower() == 'yes'
    length = int(input("What should be the length of the usernames? (minimum 3): "))
    
    if length < 3:
        print("Length must be at least 3. Setting length to 3.")
        length = 3
    
    usernames = generate_multiple_usernames(count, include_numbers, include_special_chars, length)
    
    print("\nGenerated Usernames:")
    for username in usernames:
        print(username)
    
    save_to_file = input("\nWould you like to save these usernames to a file? (yes/no): ").strip().lower()
    if save_to_file == 'yes':
        save_usernames_to_file(usernames)

if __name__ == "__main__":
    main()

