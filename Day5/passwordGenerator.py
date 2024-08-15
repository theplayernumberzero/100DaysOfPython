import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password: ")) 
nr_symbols = int(input(f"How many symbols would you like: "))
nr_numbers = int(input(f"How many numbers would you like: "))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = []
password_string = ""
for number in range(0,nr_letters):
    password.append(random.choice(letters))
for number in range(0,nr_symbols):
    password.append(random.choice(symbols))
for number in range(0,nr_numbers):
    password.append(random.choice(numbers))
for x in password:
    password_string += x
print(password_string)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_hard = random.shuffle(password)
password_string_hard = ""
for x in password:
    password_string_hard += x
print(password_string_hard)
