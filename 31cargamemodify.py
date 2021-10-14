is_started = False
while True:
    word = input('> ').lower()
    if word == ('help'):
        print('''>start => to start the Car
>stop => to stop the Car
>quit => to quit the Game
        ''')
    elif word == 'start':
        if is_started:
            print("Car is already started")
        else:
            is_started = True
            print("Car is started")
    elif word == 'stop':
        if not is_started:
            print("Car is already stopped")
        else:
            is_started =False
            print("Car is stopped")
    elif word == 'quit':
        break
    else:
        print("I don't understand that")
