#Average of students heights

student_heights = input('Input of student heights ').split()

total = 0
count = 0

for n in range (0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    total += student_heights[n]
    count += 1

print(student_heights)
print(total)
print(count)

avg = total/count

print(f'The average of the student heights is {avg}')