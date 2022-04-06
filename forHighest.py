student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

studentScores = 0
for i in range(0, len(student_scores)):
    if studentScores < student_scores[i]:
        studentScores = student_scores[i]

print(f"The highest score in the class is: {studentScores}")