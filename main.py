import random

win_lose =  [('Scissors', 'Paper'), 
                    ('Paper', 'Rock'), 
                    ('Rock', 'Lizard'),
                    ('Lizard', 'Spock'),
                    ('Spock', 'Scissors'),
                    ('Scissors', 'Lizard'),
                    ('Lizard', 'Paper'),
                    ('Paper', 'Spock'),
                    ('Spock', 'Rock'),
                    ('Rock', 'Scissors')]

print ('1 for Single player or 2 for multiplayer')
user_input = int(input('Choose 1 or 2: '))
choices = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

ai_choice = random.choice(choices)

print('Please choose one of the choices below')
print (' 0 for Rock\n 1 for Paper\n 2 for Scissors\n 3 for Lizard\n 4 for Spock\n')
 
user_input = int(input(' Your choice (0-4): ')) 
print (ai_choice)
human_choice = choices[user_input]

if ai_choice == human_choice:
    result = 'Draw!'

elif (human_choice, ai_choice) in win_lose:
    result = 'You Won!'

else: 
    result = 'You Lost'

    