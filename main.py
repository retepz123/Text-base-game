import os

player = {
    'name': '',
    'money': 250,
}

player['name'] = input('Write your name\n')

def prompt():
    print("Welcome to our World\nLife Simulator is a text-based adventure game where the player starts as a young person with limited money and must make choices that affect their future\n\n")
    input("Press enter to continue....")


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


places = {
    'House': {'South': 'Mall', 'North': 'University', 'East': 'FastFood'},
    'Mall': {
        'North': 'House'
    },
    'University': {
        'South': 'House'
    },
    'FastFood': {
        'West': 'House'
    }
}

items = {
    '1': 'Clothes - $10', '2': 'Caps - $5', '3': 'Shoes - $12'
}

current_place = 'House'
money = 200

clear()
prompt()


clear()
    
print(f"Hi {player['name']},\nMoney: ${player['money']}\n")

print(f'You probably wondering what you gonna do first, so your current place now is in your {current_place}')


while True:
    
    directions = places[current_place]
    
    for direction in directions:
        print(f"{direction} - {directions[direction]}")
    
    move = input(f'Which way you go?\n').title()
    
    #directions
    if move in directions:
        current_place = directions[move]
        print(f'\nYou have travelled to the {current_place}\n')
    else:
        print('Invalid Commands')
        
        #from House to Mall or Mall to House
    if current_place == 'Mall':
        money -= 10 #cost of the transportation
        print(f'You have cost $10 for the bus\ncurrent Money: {money}\n')
        
    elif current_place == 'House':
         money -= 10 #cost of the transportation
         print(f'You have cost $10 for the bus\ncurrent Money: {money}\n')
        
    else:
        print('Invalid keywords')
        
    print({'-' * 27})    
    print(f'Welcome to the {current_place}')
    print('There are things a lot to buy here.')
    
    
    
    