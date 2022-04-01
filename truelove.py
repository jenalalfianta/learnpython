"""
for love scores less than 10 or greater than 90
your score is x, you go together like coke and mentos.

40 and 50
your score is y, you are alright together.

your score is z.

lower()
count("hurufnya")

cek jumlah string nama dengan string pilihan truelove 
"""

from re import T


print("Welcome to the Love Calculator!")
name1 = input("What is your name? ")
name2 = input("What is their name? ")


cN = name1.lower()+name2.lower()

t = 0
r = 0
u = 0
e = 0
l = 0
o = 0
v = 0
e = 0

score = 0
if score < 10 and score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
