import string
import secrets

#Function to generate a secure random password
def generate_password(length):

#Check that the password length is at least 3
 
    if length < 3:
        raise ValueError("Password length must be at least 3.")
#Get letters,numbers, and special characters.

    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

#Add at least one letter, one number, and one symbol

    password = [
        secrets.choice(letters),
        secrets.choice(numbers),
        secrets.choice(symbols)
    ]
#Combine all possible characters

    all_characters = letters + numbers + symbols

# Generate the remaining characters randomly
    for _ in range(length - 3):

        password.append(secrets.choice(all_characters))

# Shuffle the password so the character types are in random positions
    
    secrets.SystemRandom().shuffle(password)


# Convert the list of characters into a string

    return ''.join(password)


print("===============================================================")
print("                    PASSWORD GENERATOR")
print("===============================================================")

# Keep the program running until the user chooses to exit

while True:

    try:
# Ask the user to enter the desired password length        
        length = int(input("\nEnter password length: "))

 # Check the minimum password length

        if length < 3:
            print("Password must contain at least 3 characters.")
            continue
# Generate the password
        password = generate_password(length)

# Display the generated password and its length

        print("\nGenerated Password:", password)
        print("Password Length:", len(password))

 # Handle invalid input such as letters instead of numbers
    except ValueError:

        print("Please enter a valid number.")
        continue

    # Ask the user whether they want to generate another password

    choice = input("\nGenerate another password? (y/n): ").lower()
    
 # Exit the program if the user does not enter 'y'


    if choice != "y":
        print("\nThank you for using Password Generator!")
        break  

          