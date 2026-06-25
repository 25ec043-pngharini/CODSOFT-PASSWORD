import random

print("===== PASSWORD GENERATOR =====")

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*"

all_characters = letters + numbers + symbols

length = int(input("Enter the password length: "))

password = ""

for i in range(length):
    random_character = random.choice(all_characters)
    password = password + random_character

print("\nGenerated Password:", password)

print("\nPassword Generated Successfully!")