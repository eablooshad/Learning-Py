#Password Generator

import random, string

uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
signs = string.punctuation
digits = string.digits

all_string = ''

upper, lower, num, sym = True, True, True, True

if upper:
    all_string += uppercase_letters

if lower:
    all_string += lowercase_letters

if num:
    all_string += digits

if sym:
    all_string += signs

length = 40
how_many_times = 10

# seed = 'Blooszn'
# random.seed((seed))

for x in range(how_many_times):
    gen_password = ''.join(random.sample(all_string, length))
    print(gen_password)