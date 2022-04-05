from random import random

names_string = input("Give me everybody's name, seperated by a comma.\n")
names = names_string.split(",")

name = round(random.random() * (len(names) - 1))

print(f"{names[name].strip()} is going to uy the meal today !")