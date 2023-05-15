import random
from hangman_art import *
from hangman_words import word_list

end_of_game = False
# word_list = ['ardvark', 'baboon', 'camel']
chosen_word = random.choice(word_list)

print(logo)

# testing code
print(f'the solution is {chosen_word}')

# Create Blanks
display = []

word_length = len(chosen_word)

lives = 6

for char in chosen_word:
    display += '_'
print(display)


while not end_of_game:
    guess = input('Guess a letter: ').lower()

    if guess in display:
        print(f'You tried the letter {guess}, Try a different letter!')

    for position in range(word_length):
        char = chosen_word[position]
        if char == guess:
            display[position] = char

    if guess not in chosen_word:
        lives -= 1
        print(f'You guessed the letter {guess}, That\'s not in the word, You have {lives} lives left')
        if lives == 0:
            end_of_game = True
            print('You Lose!!')

    print(f'{" ".join(display)}')

    if '_' not in display:
        end_of_game = True
        print('You Win!')

    print(stages[lives])