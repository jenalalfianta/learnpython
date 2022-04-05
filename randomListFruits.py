#https://docs.python.org/3/tutorial/datastructures.html#
import random

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
random1 = round(random.random() * (len(fruits)-1))
print(fruits[random1])

fruits.insert(1,"jenal")
fruits.remove("apple")
print(fruits)