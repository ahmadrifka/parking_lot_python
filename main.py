from garage import Garage
print('WELCOME TO PARKING LOT APP')
print('There\'s some command that you can use to play this app')
print('====================================')
print('List of Command: ')
print('1. create_parking_lot (slot number):  to create parking lot based on slot number')
print('2. park KA-001-1234 : to park car into parking lot')
print('3. leave KA-001-1234 : to remove car from lot')
print('4. status: to see parking status ')
print('5. help: to see all command list')
print('6. exit: to quit')
play = True
while play:
    inputValue = input('Please write command line: ')
    splitData = inputValue.split(' ')
    splitData[0]= splitData[0].lower()
    try:
        if splitData[0] == 'create_parking_lot':
            parking_lot = Garage(int(splitData[1]))
        elif splitData[0] == 'park':
            parking_lot.park(splitData[1])
        elif splitData[0] == 'leave':
            parking_lot.leave(splitData[1])
        elif splitData[0] == 'status':
            parking_lot.status()
        elif splitData[0] == 'exit':
            play = False
        elif splitData[0] == 'help':
            print('List of Command: ')
            print('1. create_parking_lot (slot number):  to create parking lot based on slot number')
            print('2. park KA-001-1234 : to park car into parking lot')
            print('3. leave KA-001-1234 : to remove car from lot')
            print('4. status: to see parking status ')
            print('5. help: to see all command list')
            print('6. exit: to quit')
        else:
            print('Invalid Command')
    except:
        print('No parking lot, must be create parking lot first')

