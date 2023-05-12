#Pizza order menu system
print('''
Welcome to bloo\'s pizza
**MENU**
-Size-
Small - $15
Medium - $20
Large - $25

-Extras-

pepperoni for Small Pizza - +$2
pepperoni for Medium or Large pizza - +$3
extra cheese for any pizza - +$1
''')

bill = 0

size = input('What size of pizza do you want? S/M/L ')

if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25
else:
    bill += 0

add_pepperoni = input('Do you want pepperoni? Y/N ')

if add_pepperoni == 'Y':
    bill += 2
else:
    bill += 0


extra_cheese = input('Do you want extra cheese? Y/N ')

if extra_cheese == 'Y':
    bill += 1
else:
    bill += 0

print(f'Your Bill is ${bill}')