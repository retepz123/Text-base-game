import os

name = input('Write your name\n')

def prompt():
    print("Welcome to our World")
    input("Press enter to continue....")


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


places = {
    'House': {'North': 'University', 'South': 'Mall', 'East': 'Company'},
    'Mall': {'North': 'House', 'South': 'Park'},
    'University': {'North': 'Professional Work'},
    'Professional Work': {'South': 'House'}
}

current_place = 'House'
money = 200

clear()
prompt()


clear()
    
print(f"Hello, {name},")
print(f"You are in the {current_place}")
print(f"Money: {money}\n\nFrom here you can choice your next move. you cann choose 'Mall', 'Univeristy' or to have a part-time job" )



