from random import randint

#Loop  
loop = True
while loop:
  #print main menu 
  print('\nMain Menu')
  print('1: Roll Dice Once')
  print('2: Roll Dice 5 Times')
  print('3: Roll Dice n Times')
  print('4: Roll Dice until Snake Eyes')
  print('5: Exit')

  #Selection 
  selection = input("Enter selection (1-5): ")

  #Use
  if selection == '1':
    print('\nRoll Dice Once')
    #Roll Dice once 
    print("You rolled",randint(1,6)) 

  elif selection == '2': 
    print('Roll Dice 5 Times')
    #Roll Dice 5 Times
    repeat = True
    for x in range(0, 5):
      print("You rolled",randint(1,6)) 

  elif selection == '3':
    print('Roll Dice n Times')
    #Roll Dice N Times
    total_count = int(input("how many rolls? "))
    for n in range(total_count):
      print("Dice rolled ", total_count, "times")

  elif selection == '4': 
    print('Roll Dice until Snake Eyes')
    #Snake Eyes
    total_count = 0
    range_num = 12
    for i in range(range_num):
      while True:
        total_count += 1 
        d1, d2, = randint(1,6), randint(1,6) 
        print('dice 1:', d1, 'dice 2:', d2)
        if d1 == 1 and d2 == 1:
          break 
  
  elif selection == '5':
    #Exit
    print('Exit')
    loop = False  