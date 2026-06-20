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
        'North': 'House', 'South': 'Ammusement Park'
    },
    'University': {
        'South': 'House'
    },
    'FastFood': {
        'West': 'House'
    }
}

current_place = 'House'

clear()
prompt()


clear()
    
print(f"Hi {player['name']},\nMoney: ${player['money']}\n")

print(f'You probably wondering what you gonna do first, so your current place now is in your {current_place}')


while True:
    
    
    directions = places[current_place]
    
    print(f'\nWelcome to your {current_place}')
    
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
        player['money'] -= 10 #cost of the transportation
        print(f'You have cost $10 for the bus\ncurrent Money: {player['money']}\n')
        
    elif current_place == 'House':
         player['money'] -= 10 #cost of the transportation
         print(f'You have cost $10 for the bus\ncurrent Money: {player['money']}\n')
        
    else:
        print('Invalid keywords')
        
    def mall():
        while True:
            print({'-' * 27})    
            print(f'Welcome to the {current_place}')
            print('There are things a lot to buy here.\n')
            print('1. Clothes - $30')
            print('2. Shoes - $45')
            print('3. Caps - $22')
            print('4. Winter Jacket - $70')
            print('5. Leave the Mall')
        
            choice = input('\n\nWhat do you want to buy?\n\n')
        
            if choice == '1':
                player['money'] -= 30
                print("You've purchased the clothes")
            elif choice == '2':
              player['money'] -= 45
              print("You've purchased the branded Shoes")
            elif choice == '3':
              player['money'] -= 22
              print("You've purchased the Basketball Cap")
            elif choice == '4':
                 player['money'] -= 70
                 print("You've purchased the Winter Jacket")
            elif choice == '5':
                break
            
    if current_place == 'Mall':
        mall()
        
    print(f"leaving the Mall you current money is ${player['money']}")