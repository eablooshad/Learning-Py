# BMI Calculator

# formula = weight/height^2

print('Welcome to BMI Calculator')

weight = int(input('Input weight in kg ? '))
height = float(input('Input height in m ? '))

bmi = weight//height**2

result = print(f'Your BMI is {bmi}')