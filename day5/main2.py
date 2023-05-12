# sum of all even numbers

digit = int(input('the highest number you can think of >'))
'''
sum_of_even_numbers = 0
for n in range(0, digit, 2):
    sum_of_even_numbers += n
sum_of_even_numbers += digit
'''

total = 0
digit += 1

for n in range(0, digit):
    if n % 2 == 0:
        total += n

# print(f'The sum of even numbers from 0 to {digit}, is {sum_of_even_numbers}')
print(total)