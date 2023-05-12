#Band-Name-Generator
import random

print(f'Welcome to Band Name Generator')

extension = ['Cartel', 'Gang', 'Pipers']
xtsn = random.choice(extension)

location = str(input(f'Where are you from ? '))
pet = str(input(f'whats your pet\'s name ? '))

band_name = location + pet + xtsn

print(f'Your band name could be {band_name}')
