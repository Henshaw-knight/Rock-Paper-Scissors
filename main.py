"""A Python program demonstrating Rock-Paper-Scissors game"""

import random
options = ['R', 'P', 'S']

restart = True
while restart:
    player_option = input("Pick an option R, P or S: ").upper()
    CPU = random.choice(options)
    if player_option in options:
        if player_option == 'R' and CPU == 'P':
            print('Player (Rock) : CPU (Paper)')
            print('You lose')
            restart = False
        elif player_option == 'R' and CPU == 'S':
            print('Player (Rock) : CPU (Scissors)')
            print('You win')
            restart = False
        elif player_option == 'P' and CPU == 'S':
            print('Player (Paper) : CPU (Scissors)')
            print('You lose')
            restart = False
        elif player_option == 'P' and CPU == 'R':
            print('Player (Paper) : CPU (Rock)')
            print('You win')
            restart = False              
        elif player_option == 'S' and CPU == 'R':
            print('Player (Scissors) : CPU (Rock)')
            print('You lose')
            restart = False 
        elif player_option == 'S' and CPU == 'P':
            print('Player (Scissors) : CPU (Paper)')
            print('You win')
            restart = False
        else:
            print(f'\nPlayer ({player_option}) : CPU ({CPU})')
            print('There is a tie\n')
            continue
    else:
        print('Invalid option, enter right option next time\n')
        restart = True                   

 

