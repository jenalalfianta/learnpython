#program should print each number form 1 to 100 in turn
#when the number is divisible by 3 then instead of printing the number it should print "Fizz"
#when the number is divisible by 5 then instead of printing the number it should print "Buzz"
#and if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)