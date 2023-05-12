# BMI Calculator with comment on your health situation

# formula = weight/height^2

print('Welcome to BMI Calculator')

weight = int(input('Input weight in kg ? '))
height = float(input('Input height in m ? '))

bmi = weight//height**2

comment = 'Invalid Entry'

if (bmi <= 18.5) :
    comment = 'You\'re underweight!'
elif (18.5 > bmi <= 25):
    comment = 'You have a normal weight!'
elif (25 > bmi <= 30):
    comment = 'You\'re overweight!'
elif (30 > bmi <= 35):
    comment = 'You\'re obese!'
else:
    comment = 'You\'re clinically obese!'

result = print(f'Your BMI is {bmi}, {comment}')