import random
import string

password_length = int(input("Enter the length of the password you want to generate: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(characters) for i in range(password_length))

print("Your generated password is:", password)
