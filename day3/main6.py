#Treasure island

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
''')

print('Welcome to Treasure Island. \nYour mission is to find the treasure.')

choice = input('''
Make your choice? Left or Right
''').lower()

if choice == 'left':
    choice = input('''
    You got to the river side, what are you going to do now? Swim or Wait
    ''').lower()

    if choice == 'wait':
        choice = input('''
        You\'ve waited long enough for sunset, The doors have shown themselves.\n which door are you going through Red, Yellow, Blue
        ''').lower()

        if choice == 'yellow':
            print('''
      __________________
    .-'  \ _.-''-._ /  '-.
  .-/\   .'.      .'.   /\-.
 _'/  \.'   '.  .'   './  \'_
:======:======::======:======:  
 '. '.  \     ''     /  .' .'
   '. .  \   :  :   /  . .'
     '.'  \  '  '  /  '.'
       ':  \:    :/  :'
         '. \    / .'
           '.\  /.'  
             '\/'

            Victor!! The Treasure of a thousand years has been found, You Win!
            ''')
        elif choice == 'red':
            print('''
            You entered the den of fire, You were Burnt to death.
            Game Over.
            ''')
        elif choice == 'blue':
            print('''
            You entered the den of the Beasts, You fought till death!
            Game Over.
            ''') 

    else:
        print('''
        You swam to the crocodiles den.
        Game Over.
        ''')

else:
    print('''
    You Fell to your death into a hole.
    Game Over.
    ''')