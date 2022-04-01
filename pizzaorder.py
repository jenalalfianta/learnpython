smallPizza = 15
mediumPizza = 20
largePizza = 25
pepperoniSmallPizza = 2
pepperoniMediumOrLargePizza = 3
extraCheese = 1
total = 0
pizzaType = ""

print("Welcome to Python Pizza Deliveries!")

#pick pizza size
size = input("What size pizza do you want (S,M,L)? ")
if size == "s" or size == "S":
    total+=smallPizza
    pizzaType = "s"
elif size == "m" or size == "M":
    total+=mediumPizza
    pizzaType = "m"
elif size == "l" or size == "L":
    total+=largePizza
    pizzaType = "l"
else:
    print("sorry, you input wrong answer!")
    exit()

#add pepperoni
add_pepperoni = input("Do you want pepperoni (Y/N)? ")
if add_pepperoni == "y" and pizzaType == "s" or add_pepperoni == "Y" and pizzaType == "s":
    total += pepperoniSmallPizza
elif (add_pepperoni == "y" and pizzaType == "m" or add_pepperoni == "Y"  and pizzaType == "m" or 
    add_pepperoni == "y" and pizzaType == "l" or add_pepperoni == "y" and pizzaType == "L"):
    total += pepperoniMediumOrLargePizza
else:
    total += 0

#add cheese
extra_cheese = input("Do you want extra cheese (Y/N)?")
if extra_cheese == "y" or extra_cheese == "Y":
    total+=extraCheese
else:
    total += 0

print(f"Your final bill is: ${total}.")