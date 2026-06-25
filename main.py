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


#specific current places Random Events
def mall_random_events():
    mall_random = ['🎟️ You won a raffle prize!',
                   '🛍️ Huge sale! You spent extra money.',
                   '☕ You enjoyed coffee with friends.',
                   '📱 You found a discount coupon.']
    
    random_mall = random.choice(mall_random)
    
    print('\n==== What is Happening? ====\n')
    print(random_mall)
    input('\nPress Enter to Continue ....\n')
    
    
    if random_mall == '🎟️ You won a raffle prize!':
        player['money'] += 50
        
    elif random_mall == '🛍️ Huge sale! You spent extra money.':
        player['money'] -= 20
        
    elif random_mall == '☕ You enjoyed coffee with friends.':
        player['money'] -= 5
        player['Happines'] += 5
        player['stress'] -= 5
        
    elif random_mall == '📱 You found a discount coupon.':
        player["Happines"] += 3
        
    print(f"""\n
        Money: ${player['money']}
        Happiness: {player['Happines']}%
        Stress: {player['stress']}%
        \n""")


def part_time_random_events():
    random_partTime = ['💵 Customer tipped you $20.',
                       '⭐ You received positive feedback.',
                       '😡 Difficult customer ruined your mood.',
                       '🚲 Bike tire got damaged.',
                       '🎁 Your manager gave you a bonus.']
    
    partTime_random = random.choice(random_partTime)
    
    print('\n==== It happens all the time ====\n')
    print(partTime_random)
    input('\nPress Enter to Continue ....\n')
    
    
    if partTime_random == '💵 Customer tipped you $20.':
        player['money'] += 20
        
    elif partTime_random == '⭐ You received positive feedback.':
        player["Happines"] += 5
        
    elif partTime_random == '😡 Difficult customer ruined your mood.':
        player['Happines'] -= 5
        player['stress'] += 15
        
    elif partTime_random == '🚲 Bike tire got damaged.':
        player["money"] -= 13
        player['stress'] += 5
        
    elif partTime_random == '🎁 Your manager gave you a bonus.':
        player['Happines'] += 7
        player['money'] += 50
        
    print(f"""\n
        Money: ${player['money']}
        Happiness: {player['Happines']}%
        Stress: {player['stress']}%
        \n""")
    input('Press Enter to Continue ....')
    
    
def prof_work_random():
    work_random = ['⏰ Overtime increased your stress.',
                   '🎉 Company team-building event.',
                   '💼 Your boss praised your work.',
                   '💰 Performance bonus received.']
    
    workRandom = random.choice(work_random)
    
    print('\n===== Sometimes this happened each company =====\n')
    print(workRandom)
    input('\nPress Enter to Continue ....\n')

    if workRandom == '⏰ Overtime increased your stress.':
        player['stress'] += 7
        
    elif workRandom == '🎉 Company team-building event.':
        player['Happines'] += 10
        
    elif workRandom == '💼 Your boss praised your work.':
        player['Happines'] += 5
        
    elif workRandom == '💰 Performance bonus received.':
        player['Happines'] += 5
        player['money'] += 50
        
    print(f"""\n
        Money: ${player['money']}
        Happiness: {player['Happines']}%
        Stress: {player['stress']}%
        \n""")

def university_random():
    univ_random = ['📚 Surprise quiz!',
                  '🤝 You joined a study group.',
                  '😴 You overslept and missed a class.',
                  '📝 Your project received high marks.']

    random_univ = random.choice(univ_random)
    
    print('=====  Random Situations in University  =====')
    print(random_univ)
    input('\nPress Enter to Continue ...\n')

    
    
    if random_univ == '📚 Surprise quiz!':
        player['stress'] += 5
        
    elif random_univ == '🤝 You joined a study group.':
        player['Happines'] -= 5
        
    elif random_univ == '😴 You overslept and missed a class.':
        player['stress'] += 5
        
    elif random_univ == '📝 Your project received high marks.':
        player['Happines'] += 5
        
    print(f"""\n
        Money: ${player['money']}
        Happiness: {player['Happines']}%
        Stress: {player['stress']}%
        \n""")
    
def funland_random_events():
    funland_random = ['🎢 Front-row roller coaster ride!',
                      '🎯 You won a giant stuffed toy.',
                      '🍦 Free ice cream!',
                      '📸 You took memorable photos.']
    
    random_funland = random.choice(funland_random)
    
    print('===== Random Situations in Funland Park =====')
    print(random_funland)
    input('\nPress Enter to Continue ....\n')
    
    
    if random_funland == '📸 You took memorable photos.':
        player['Happines'] += 5
        
    elif random_funland == '🎢 Front-row roller coaster ride!':
        player['Happines'] += 5
        
    elif random_funland == '🎯 You won a giant stuffed toy.':
        player['Happines'] += 5
        
    elif random_funland == '🍦 Free ice cream!':
         player['Happines'] += 5
    
    print(f"""\n
        Money: ${player['money']}
        Happiness: {player['Happines']}%
        Stress: {player['stress']}%
        \n""")
        
        
#random event
def randomEvent():
    events = ['💰 You found $20 on the street!',
             '🎉 You met an old friend and feel happier!',
             '🍔 Someone bought you a free meal.',
             '😓 You lost your wallet.',
             '💸 You accidentally broke something and paid for repairs.',
             '👨‍👩‍👧 Your parents gave you $50 allowance.',]
    
    event = random.choice(events)
    
    print('\n==== Random Event ====\n')
    print(event)
    input('\nPress Enter to Continue ....\n')
    
    
    if event == '💰 You found $20 on the street!':
        player['money'] += 20
        
    elif event == '🎉 You met an old friend and feel happier!':
        player['Happines'] += 10
        
    elif event == '🍔 Someone bought you a free meal.':
        player['Happines'] += 5
        
    elif event == '😓 You lost your wallet.':
        player['money'] -= 17
        
    elif event == '👨‍👩‍👧 Your parents gave you $50 allowance.':
        player['money'] += 50
        
    elif event == '💸 You accidentally broke something and paid for repairs.':
        player['money'] -= 30
        player['stress'] += 5
        player['Happines'] -= 7
        
    print(f"""\n
        Money: ${player['money']}
        Happiness: {player['Happines']}%
        Stress: {player['stress']}%
        \n""")

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
        print(f'\n\n{'🎡' * 5} Welcome to the Fun Land Ammusment Park {'🛝' * 5}\n\n')
        print('In ammusement park it will increase your Happines and decrease your stress\n')
        print('1. Ferris Wheel')
        print('2. Roller Coaster')
        print('3. Arcade')
        print('4. Shooting Game')
        print('5. Leave')
        
        choice = input('Choose:\n')
        
        if choice == '5':
            break
        elif choice == '1':
            player['money'] -= 5
            player['Happines'] += 10
            player['stress'] -= 5
            print(f'\nSeeing the overlooking view it increase my Happiness\n\nHappines: {player['Happines']}%')
        elif choice == '2':
            player['money'] -= 12
            player['stress'] += 5
            print(f"\nI've been holding my breath during the ride it was amazing, I think my stress was increase\n\nStress: {player['stress']}%")
        elif choice == '3':
            player['money'] -= 2
            player['Happines'] += 5
            player['stress'] -= 5
            print(f'\nThis Arcade its is better it chills me.\n\nHappiness: {player['Happines']}%\nStress: {player['stress']}%\n')
        elif choice == '4':
            player['money'] -= 5
            player["Happines"] += 5
            player['stress'] -= 2
            print(f'\nI am good in this shooting game\n\nHappiness: {player['Happines']}%\nStress: {player['stress']}%\n')

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
        roll = random.randint(1, 50)
       
        if roll <= 15:
            randomEvent()

        elif roll <= 30:
            if current_place == 'Mall':
                mall_random_events()

            elif current_place == 'Part-time Job':
                part_time_random_events()
            
            elif current_place == 'Professional Work':
                prof_work_random()
                
            elif current_place == 'University':
                university_random()
            
        
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