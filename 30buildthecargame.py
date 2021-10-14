i = 1
while i > 0:
    i = +1
    word = input('> ')
    if word.lower() == ('help'):
        print('''>start => to start the Car
>stop => to stop the Car
>quit => to quit the Game
        ''')
    elif word.lower() == 'start':
        print('Car started..Ready to go!')
    elif word.lower() == 'start':
        print('Car already started')
    elif word.lower() == 'stop':
        print('Car stopped.')
    elif word.lower() == 'stop':
        print('Car ALready stopped')
    elif word.lower() == 'quit':
        break
    else:
      print("I don't understand that")
