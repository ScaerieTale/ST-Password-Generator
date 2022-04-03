'''This code was written in part under the guidance of Dr. Angela Yu of the London App Brewery
and as such is 100% CC Zero.  I hope you're able to find it as useful as I did learning to 
write it! ♥
-- ScaerieTale'''

import random
import sys
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# ScaerieTale's code #

password = ""
for char in range(1, nr_letters + 1):
    password = password + random.choice(letters)
for sym in range(1, nr_symbols + 1):
    password = password + random.choice(symbols)
for nums in range(1, nr_numbers + 1):
    password = password + random.choice(numbers)
print(f"Your password: {''.join(random.sample(password,len(password)))}")
input("Don't forget to write down or copy it!")