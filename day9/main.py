# Understanding Dictionary

programming_dictionary = {
    'Bug' : 'An error in a program that prevents the program from running as expected.',
    'Function' : 'A piece of code that you can easily call over and over again.',
    'Loop' : 'The action of doing something over and over again.',
}

# Retrieving items from the dictionary
# print(programming_dictionary['Bug'])

# Adding new items to tthe dictionary
# programming_dictionary['Run'] = 'The process of making your piece of code perform its use.'

# create an empty dictionary
# empty_dictionary = {}

# wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in the dictionary
# programming_dictionary['Bug'] = 'A moth in your computer.'
# print(programming_dictionary)

# loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])