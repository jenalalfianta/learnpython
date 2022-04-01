"""
http://math.ipb.ac.id/index.php?option=com_content&task=view&id=245
Tahun kabisat adalah tahun yang habis dibagi 4 
namun tidak habis dibagi seratus
atau tahun yang habis dibagi 400
"""

year = int(input("Which year do you want to check? "))
leap = 0

if year % 4 == 0:
    leap += 1

if year % 100 == 0:
    leap = leap
else:
    leap += 1

if year % 400 == 0:
    leap += 1

if leap > 1:
    print("leap number !")
else:
    print("sorry is't leap number")