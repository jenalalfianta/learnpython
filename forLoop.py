# buahBuahan = ["Mangga", "Apel", "Jeruk"]
# for buah in buahBuahan:
#     print(buah)

# student_heihts = [180, 124, 165, 173, 189, 169, 146]
# totalHeight = 0

# for height in student_heihts:
#     totalHeight += height

# averageHeight = totalHeight/len(student_heihts)

# print(f"Average Height is {round(averageHeight,2)}")


a = []
student_heihts = input("Input a list of student heights ").split()
for n in range(0, len(student_heihts)):
    a = int(student_heihts[n])
print(student_heihts)
print(a)