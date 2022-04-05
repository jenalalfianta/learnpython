import random

choose = input("tail or head ?\n")
result = round(random.random() * 1)
temp = ""

if result == 0:
    temp = "tail"
else:
    temp = "head"

if choose == temp:
    print("wow, nice picking..")
else:
    print("you're wrong..")