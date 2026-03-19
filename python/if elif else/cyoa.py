print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("You\'re at a crossroad, where do you want to go? "
                "Type 'left' or 'Right'.").lower()

if choice1 == 'left':
    choice2 = input("You\'ve come to a lake. "
                    "Type 'wait' to wait for a boat. "
                    "Type 'swim' to swim across. ").lower()
    if choice2 == 'wait':
        choice3 = input('You arrive at a series of doors. '
                        'One red, one blue and one yellow. '
                        'Which door has the treasure behind it? ').lower()
        if choice3 == 'red':
            print('The room is on fire. Game Over!')
        elif choice3 == 'blue':
            print('The room is freezing. Game Over!')
        elif choice3 == 'yellow':
            print('Congratulations! You found the gold!')
        else:
            print('What? Game Over!')
    else:
        print('You were eaten by an angry trout! Game Over!')
else:
    print('You fell into a hole. Game Over')