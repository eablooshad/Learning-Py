# life in weeks

your_age = int(input('How old are you?'))

your_age_in_days = your_age * 365
your_age_in_weeks = your_age * 52
your_age_in_months = your_age * 12

print(f'you are {your_age} years old, & you\'ve lived for {your_age_in_months} months,you {your_age_in_weeks} weeks, {your_age_in_days} days')

till_ninety = 90
till_ninety_in_days = 90 * 365
till_ninety_in_weeks = 90 * 52
till_ninety_in_months = 90 * 12

print(f'you have {till_ninety - your_age} years, {till_ninety_in_months - your_age_in_months} months, {till_ninety_in_weeks - your_age_in_weeks} weeks, {till_ninety_in_days - your_age_in_days} days left.')