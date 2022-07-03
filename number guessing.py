import random

point = 0
while True:
    print("Guess a randomly generated number. Enter 0 to exit the game.")
    number = random.randrange(1, 10)
    #print(number) - this line is to check whether the game is creating random numbers or not.
    guess = int(input("Guess the number: "))
    if guess == number:
        print("You guessed it right")
        point += 1
        print("Points: {}".format(point))
    elif guess == 0:
        print("Points: {}".format(point))
        break
    else:
        print("wrong")
        point -= 1
        print("Points: {}".format(point))
