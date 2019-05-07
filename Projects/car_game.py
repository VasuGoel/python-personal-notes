help_message = '''start - to start the car
stop - to stop the car
quit - to quit the program'''

car_started = False;
car_stopped = False;

command = ""
while True:
    command = input('> ')
    if command.lower() == 'start':
        if car_started == False:
            print('Car started. Ready to go!')
            car_started =  True
            car_stopped = False
        else:
            print('Car is already started.')
    elif command.lower() == 'stop':
        if car_stopped == False and car_started == True:
            print('Car stopped.')
            car_stopped = True
            car_started = False
        else:
            print('Car is already stopped.')
    elif command.lower() == 'help':
        print(help_message)
    elif command.lower() == 'quit':
        print('See you later.')
        quit()
    else:
        print('I\'m not sure I follow... Type \'help\' to see list of commands.')
