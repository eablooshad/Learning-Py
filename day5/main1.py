# identify the highest score in the list
student_scores = input('input a list of students ').split()

highest = int(student_scores[0])
lowest = int(student_scores[0])

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

for score in student_scores:
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score
    
print(student_scores)
print(highest)
print(lowest)