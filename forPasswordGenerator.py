import random

letters  = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers  = ['0','1','2','3','4','5','6','7','8','9']
symbols  = ['!','#','$','%','&','(',')','*','+', '@']

print("Welcome to the PyPassword Generator!")
nr_letters   = int(input("How many letters would you like in your password? "))
nr_numbers   = int(input("How many numbers would you like in your password? "))
nr_symbols   = int(input("How many symbols would you like in your password? "))

totalChar    = nr_letters + nr_symbols + nr_numbers 
tempPassword = []
password     = ""

for _ in range(1, totalChar + 1):
    if _ <= nr_letters:
        tempPassword.append(letters[random.randint(0, len(letters) - 1)])
    
    if _ <= nr_numbers:
        tempPassword.append(numbers[random.randint(0, len(numbers) - 1)])

    if _ <= nr_symbols:
        tempPassword.append(symbols[random.randint(0, len(symbols) - 1)])

tempPassword = random.sample(tempPassword, len(tempPassword))

for x in range(0, len(tempPassword)):
    password += tempPassword[x]

print(f"Here is your password: {password}")