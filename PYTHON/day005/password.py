#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


symbols_list = [nr_letters, nr_symbols, nr_numbers]

total = sum(symbols_list)
password = ""
print(total)
while(total > 0):
    symbol_index = random.randint(0, 2)
    if symbols_list[symbol_index] > 0:
        if symbol_index == 0:
            password += letters[random.randint(0,len(letters)-1)]
            total -= 1 
        
        if symbol_index == 1:
            password += symbols[random.randint(0,len(symbols)-1)]
            total -= 1 
            
        if symbol_index == 2:
            password += numbers[random.randint(0,len(numbers)-1)]
            total -= 1
            
print(password)