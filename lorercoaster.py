print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
pay = 0

if height >= 120:
    print("you can ride the rollercoaster!")
    age = int(input("What is our age? "))
    if age < 12:
        pay+=5
    elif age <= 18:
        pay+=7
    else:
        pay+=12
    
    photo = input("You want to take the photo ? (Y/N)")
    if photo == "Y" or "y":
        pay+=3
    print(f"Please pay {pay}")

else:
    print("Sorry, you have to grow taller before you can ride.")