print("Welcome to the Love Calculator!")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

cN = name1.lower()+name2.lower()

t = cN.count("t")
r = cN.count("r")
u = cN.count("u")
e = cN.count("e")

l = cN.count("l")
o = cN.count("o")
v = cN.count("v")
e = cN.count("e")

sco = t+r+u+e
re = l+o+v+e
testScore= str(sco) + str(re)
score = int(testScore)

if score < 10 and score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
