#Guessing Game

count = 1
while count <= 3:
    count += 1
    num = int(input('Guess: '))
    if num == 9:
        print("You win")
        break
else:
        print("Sorry you Failed!")  
#While can also have else  