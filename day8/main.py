# calling & understanding functions
'''
name = input('What\'s your name ? ')

def greet():
    print(f'Hello {name}')
    print(f'Gm {name}')
    print(f'Hey {name}, hope you have an amamzing day!')
'''
'''
greet()

def greet_with_name(name):
    print(f'Hello {name}')
    print(f'How do you do {name}?')

greet_with_name('Billie')
'''

def greet_with(name, location):
    print(f'Hello {name}')
    print(f'What is it like in {location}')

# postional arguments
# greet_with('Tayo', 'London')

# keyword arguments
greet_with(location='Neverland', name='Ed')