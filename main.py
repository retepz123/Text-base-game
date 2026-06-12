print ('Welcome to Life Simulator')

startGame  = input('Want to play the game? Yes or No')

if startGame == 'Yes':
  print('Enjoy the Game')
  
elif startGame == 'No':
  print ('Play it when you have the guts')
  exit()
else:
  print ('Invalid Choice')
  exit()



name = input('Write your name here')

print (f'Hello, {name}!')