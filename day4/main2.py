# Dinner roulette

import random

names_str = input('type the name\'s of individuals present >> ')

names = names_str.split(', ')

# chosen_one = random.choice(names)
# print(f'{chosen_one} is paying for the meal today!')

# or

names_count = len(names)
chosen_one_int = random.randint(0, names_count - 1)
chosen_one_to_pay = names[chosen_one_int]
print(f'{chosen_one_to_pay} is paying for the meal today!')
