#ceaser cipher

from logo import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(start_text, shift_amount, ciper_direction):
    end_text = ''
    if ciper_direction == 'decode':
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text +=alphabet[new_position]
        else:
            end_text += char
    print(f'The {ciper_direction}d text is {end_text}')


'''
def encrypt(plain_text, shift_amount):
    cipher_text = ''
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f'The encoded text is {cipher_text}')

def decrypt(encrypt_text, shift_amount):
    plain_text = ''
    for letter in encrypt_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print(f'The decoded text is {plain_text}')

if direction == 'encode':
    encrypt(plain_text=text, shift_amount=shift)
elif direction == 'decode':
    decrypt(encrypt_text=text, shift_amount=shift)
else:
    print('I\'m not sure what you mean!')
'''

should_continue = True

while should_continue:
    direction = input('Type "encode" to encrypt, type "decode" to decrypt:\n')
    text = input('Input text here:\n').lower()
    shift = int(input('Type the shift number:\n'))

    #modifying the shift pattern!
    shift %= 26

    ceaser(start_text=text, shift_amount=shift, ciper_direction=direction)

    at_the_end = input('Type "yes" if you want to go again. Otherwise type "no".\n').lower()
    if at_the_end == 'no':
        should_continue = False
        print('GoodBye!')