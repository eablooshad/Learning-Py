# Tip calculator

# (bill/peeps) * (100+tip_rate/100)

print('Welcome To The Tip Calculator')

bill = int(input('What was the total bill ? '))
tip_rate = int(input('What percentage of tip would you like to give ? 10%, 12%, 15%? '))
peeps = int(input('How many people are sharing the bill? '))

individual_bill = float((bill/peeps) * ((100 + tip_rate) / 100))
final_amount = '{:.2f}'.format(individual_bill)

print(f'Each person should pay: ${final_amount}')