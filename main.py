print ('Welcome to Life Simulator')

startGame  = input('Want to play the game? Yes or No  ')

if startGame == 'Yes':
  print('Enjoy the Game')
  
elif startGame == 'No':
  print ('Play it when you have the guts')
  exit()
else:
  print ('Invalid Choice')
  exit()

name = input('Write your name here  ')
age = input('age: ')
money = 500

print (f'Hello, {name}!')
print (f'Age: {age}')
print (f'Money: {money}')

# Main game
print ('\nWelcome to Life Simulator, a text-based adventure where every decision shapes your future.')
print ('1. Take the Bus')
print ('2. Walk Straight')
print ('3. Take the Bike')
print ('4. Exit')

choice = input('Choose an option  ')

# if you choose the bus logic
if choice == '1':
  money -= 10
  print ('\n$10 fare bus')
  
  print('choose your destination')
  
  #choice for bike
elif choice == '3':
  print('Option to do it')
  print('1. Go to College and Study')
  print('2. Apply for work')
  
  #if choose the study college
  bike = input('Choose where to go:  ')
  
  if bike == '1':
    print('You are arriving in the University')
    print('You are now studying...')
    print("You've gained knowledge you are ready for work")
    
  else:
    print('nice')
  
else:
  print('End of the game')