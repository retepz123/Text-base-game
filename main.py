import os
import random

player = {"name": "", "age": "", "money": 250, "skills": False, "Happines": 50, "stress": 10}

player["name"] = input("Write your name\n")
player["age"] = input("\nInput your Age\n")


def prompt():
    print(
        "Welcome to our World\nLife Simulator is a text-based adventure game where the player starts as a young person with limited money and must make choices that affect their future\n\n"
    )
    input("Press enter to continue....")


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# dictionaries for directions
places = {
    "House": {
        "South": "Mall",
        "North": "University",
        "East": "Part-time Job",
        "North-North": "Professional Work",
        "Quit": "Leaving the game",
        "South-South": "Funland Park"
    },
    "Mall": {"North": "House", "South": "Funland Park"},
    "University": {"South": "House", "North": "Professional Work"},
    "Part-time Job": {"West": "House"},
    "Professional Work": {"South": "House"},
    "Funland Park": {"North": "House"}
}

current_place = "House"

clear()
prompt()

clear()

print(f"Hi {player['name']},\nMoney: ${player['money']}\nHappiness: {player['Happines']}%\nStress: {player['stress']}%\n\n")
print(
    f"You probably wondering what you gonna do first, so your current place now is in your {current_place}"
)

#random event
def randomEvent():
    events = ['💰 You found $20 on the street!',
             '🎉 You met an old friend and feel happier!',
             '🍔 Someone bought you a free meal.',
             '😓 You lost your wallet.']
    
    event = random.choice(events)
    
    print('\n==== Random Event ====\n')
    print(event)
    
    input('Press Enter to Continue ....')
    
    if event == '💰 You found $20 on the street!':
        player['money'] += 20
        
    elif event == '🎉 You met an old friend and feel happier!':
        player['Happines'] += 35
        
    elif event == '🍔 Someone bought you a free meal.':
        player['money'] -= 11
        
    elif event == '😓 You lost your wallet.':
        player['money'] -= 17

# Mall
def mall():
        while True:
            print({"👕👖👟" * 5})
            print(f"Welcome to the {current_place}")
            print("There are things a lot to buy here.\n")
            print("1. Clothes - $30")
            print("2. Shoes - $45")
            print("3. Caps - $22")
            print("4. Winter Jacket - $70")
            print("5. Leave the Mall\n\n")
            print('Just write the number what you choose')

            choice = input("\n\nWhat do you want to buy?\n")
            
            

            if choice == "1":
                player["money"] -= 30
                print("-- You've purchased the clothes 👕👖\n")
            elif choice == "2":
                player["money"] -= 45
                print("-- You've purchased the branded Shoes 👟\n")
            elif choice == "3":
                player["money"] -= 22
                print("-- You've purchased the Basketball Cap 🧢🧢\n")
            elif choice == "4":
                player["money"] -= 70
                print("-- You've purchased the Winter Jacket 🧥\n")
            elif choice == "5":
                break

    # print(f"You are now leaving, your current money is ${player['money']}")

    # part-time job
def partime():
        while True:
            print(f"\n{'🏍️' * 6}  Grab Company  {'🏍️' * 6} \n")
            print(
                "Your wallet is running low, and bills won't pay themselves. To earn some extra cash, you've decided to work as a food delivery rider. Every delivery brings you one step closer to financial stability.\n"
            )
            input("~ Press Enter to continue ....")

            deliver_food = input(
                "A customer has placed a food order. Deliver it to earn money. Yes or No\n"
            ).lower()

            if deliver_food == "yes":
                player["money"] += 30
                print("\n---- Succesfully delivered the food, you earned $30 ----\n\n")
            elif deliver_food == "no":
                break
            else:
                print("Invalid Command")

    # Univeristy
def univeristy():
        # only visits once
        if not player["skills"]:
            print("Welcome to the University")
            player["skills"] = True
            player['stress'] += 10
            player['Happines'] -= 10
            print(f"\n{'📔📕' * 5} ")
            print(
                "You arrive at the university campus, eager to improve your future. Every lesson you attend brings you closer to new opportunities."
            )
            input("\nPress Enter to conitue...\n")
            print("You acquired knowledge and skills, you can now work for better jobs\n")
            print(f'but it affects your status.\nYour Happiness - {player['Happines']}%\nYour Stress - {player['stress']}%\n')
            player["skills"] = True

        else:
            print("----- You are done here. -----")

    # professional work
def professional_work():
        while True:
            print(f"\n\n{'🏢' * 5}")
            print("Welcome to your work\n")
            print(
                "You arrive at the office ready to tackle new challenges. Every task you complete helps you gain experience and earn a steady income.\n"
            )

            start_work = input(
                "Are you excited to work your dream job? Yes or No\n"
            ).lower()

            if start_work == "yes":
                player["money"] += 100
                print("\n---You have earned $100---\n\n")
            elif start_work == "no":
                break


def funland_park():
    while True:
        print(f'{'🎡' * 5} Welcome to the Fun Land Ammusment Park {'🛝' * 5}\n\n')
        print('In ammusement park it will increase your Happines and decrease your stress\n')
        print('1. Ferris Wheel')
        print('2. Roller Coaster')
        print('3. Arcade')
        print('4. Shooting Game')
        print('5. Leave')
        
        choice = input('Choose: \n')
        
        if choice == '5':
            break
        elif choice == '1':
            player['money'] -= 5
            player['Happines'] += 10
            player['stress'] -= 5
            print(f'Seeing the overlooking view it increase my Happiness\nHappines: {player['Happines']}%')
        elif choice == '2':
            player['money'] -= 12
            player['stress'] += 5
            print(f"I've been holding my breath during the ride it was amazing, I think my stress was increase\nStress: {player['stress']}%")
        elif choice == '3':
            player['money'] -= 2
            player['Happines'] += 15
            player['stress'] -= 5
            print(f'This Arcade its is better it chills me.\nHappiness: {player['Happines']}%\nStress: {player['stress']}%\n')
        elif choice == '4':
            player['money'] -= 5
            player["Happines"] += 5
            player['stress'] -= 2
            print(f'I am good in this shooting game\nHappiness: {player['Happines']}%\nStress: {player['stress']}%\n')

# Main game
while True:
    directions = places[current_place]

    print(f"Welcome to your {current_place}\n")

    for direction in directions:
        print(f"{direction} - {directions[direction]}")
        
        
    move = input(f"\nWhich way you go?\n").title()

    if move == 'Quit':
        print('\nThanks for playing! Goodbye')
        break
    
    # directions
    if move in directions:
        current_place = directions[move]
        print(f"\nYou have travelled to the {current_place}\n")
        
        #random events
        if random.randint(1, 100) <= 30:
            randomEvent()
        
    else:
        print("Invalid Commands")

    
    # directions
    if current_place == "Mall":
        player["money"] -= 10  # cost of the transportation
        print(f"\nYou have cost $10 for the bus\ncurrent Money: {player['money']}\n")
        mall()
    elif current_place == "Part-time Job":
        player["money"] -= 8
        print(f"\nIt cost $8 for the bus\nYour money is now {player['money']}")
        partime()

    elif current_place == "House":
        player["money"] -= 10  # cost of the transportation
        print(f"\nYou have cost $10 for the bus\ncurrent Money: {player['money']}\n")

    elif current_place == "University":
        player["money"] -= 5
        print(f"\nYou rode the bus, it cost you $5")
        univeristy()

    elif current_place == "Professional Work":
        if player["skills"] == True:
            player["money"] -= 15
            print(
                f"\nYou've arrived to your work\nThe taxi fare is $15. Your money now is {player['money']}"
            )
            professional_work()
    
        else:
            print("--- You need to study first ---\n")
            
    elif current_place == 'Funland Park':
        player['money'] -= 20
        print(f"\nYou've arrived at the Funland Park, it cost $20 for fare\n")
        funland_park()
            
    #end of the loop
    else:
        print("Invalid keywords")