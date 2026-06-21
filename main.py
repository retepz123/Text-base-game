import os

player = {
    'name': '',
    'money': 250,
    'skills': False 
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

#dictionaries for directions
places = {
    'House': {'South': 'Mall', 'North': 'University', 'East': 'Part-time Job', 'North-North': 'Professional Work'},
    'Mall': {
        'North': 'House', 'South': 'Ammusement Park'
    },
    'University': {
        'South': 'House',
        'North': 'Professional Work'
    },
    'Part-time Job': {
        'West': 'House'
    },
    'Professional Work': {
        'South': 'House'
    }
}

current_place = 'House'

clear()
prompt()


clear()
    
print(f"Hi {player['name']},\nMoney: ${player['money']}\n")

print(f'You probably wondering what you gonna do first, so your current place now is in your {current_place}')

#Main game
while True:
    directions = places[current_place]
    
    print(f'Welcome to your {current_place}')
    
    for direction in directions:
        print(f"{direction} - {directions[direction]}")
    
    move = input(f'\nWhich way you go?\n').title()
    
    #directions
    if move in directions:
        current_place = directions[move]
        print(f'\nYou have travelled to the {current_place}\n')
    else:
        print('Invalid Commands')
    
    #Mall
    def mall():
        while True:
            print({'👕👖👟' * 5})    
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
        
    # print(f"You are now leaving, your current money is ${player['money']}")
    
    #part-time job
    def partime():
        while True:
            print(f"\n{'🏍️' * 6} Grab Company  {'🏍️' * 6} \n")
            print("Your wallet is running low, and bills won't pay themselves. To earn some extra cash, you've decided to work as a food delivery rider. Every delivery brings you one step closer to financial stability.\n")
            input('Press Enter to continue')
            
            deliver_food = input('A customer has placed a food order. Deliver it to earn money. Yes or No\n').lower()
            
            if deliver_food == 'yes':
                player['money'] += 30
                print('\nSuccesfully delivered the food, you earned $30\n\n')
            elif deliver_food == 'no':
                break
            else:
                print('Invalid Command')
    
    #Univeristy         
    def univeristy():
         #only visits once
        if not player['skills']:
            print('Welcome to the University')
            player['skills'] = True
            print(f'\n{'📔📕' * 5} ')
            print('You arrive at the university campus, eager to improve your future. Every lesson you attend brings you closer to new opportunities.')
            input('\nPress Enter to conitue...\n')
            print('You acquired knowledge and skills, you can now work for better jobs')
            player['skills'] = True
            
        else:
            print('----- You are done here. -----')
    
    #professional work
    def professional_work():
        while True:
            print(f'\n\n{'🏢' * 5}')
            print('Welcome to your work\n')
            print('You arrive at the office ready to tackle new challenges. Every task you complete helps you gain experience and earn a steady income.\n')
            
            start_work = input('Are you excited to work your dream job? Yes or No\n').lower()
            
            if start_work == 'yes':
                player['money'] += 100
                print('\n---You have earned $100---\n\n')
            elif start_work == 'no':
                break
    
    
    # directions            
    if current_place == 'Mall':
        player['money'] -= 10 #cost of the transportation
        print(f'You have cost $10 for the bus\ncurrent Money: {player['money']}\n')
        mall()
    elif current_place == 'Part-time Job':
        player['money'] -= 8
        print(f'It cost $8 for the bus\nYour money is now {player['money']}')
        partime()
        
    elif current_place == 'House':
         player['money'] -= 10 #cost of the transportation
         print(f'You have cost $10 for the bus\ncurrent Money: {player['money']}\n')
         
    elif current_place == 'University' :
        player['money'] -= 5
        print(f'You rode the bus, it cost you $5')
        univeristy()
        
    elif current_place == 'Professional Work': 
        if player['skills'] == True:
            player['money'] -= 15
            print(f"You've arrived to your work\nThe taxi fare is $15. Your money now is {player['money']}")
            professional_work()
        else:
            print('--- You need to study first ---\n')
        
        
    else:
        print('Invalid keywords')
         