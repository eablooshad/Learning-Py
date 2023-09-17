# Band-Name-Generator
import random

print(f'Welcome to Band Name Generator')

extension_choice = ['Cartel', 'Gang', 'Pipers', 'Cabal', 'Hawks']
extension = random.choice(extension_choice)

location = str(input(f'Where are you from ? '))
pet = str(input(f'whats your pet\'s name ? '))

band_name = location + ' ' + pet + ' ' + extension

print(f'Your band name could be {band_name}')
