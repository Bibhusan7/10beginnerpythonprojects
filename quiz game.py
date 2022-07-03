#quiz game
username = input("enter your username: ")
points = 0
while True:
    print("""levels-
          1.easy
          2.medium
          3.hard
          0.break
          """)
    choice = int(input(f"{username} please choose from following levels: "))
    if choice == 1:
        print("What is the capital city of India?")
        ans = input("enter your ans: ").capitalize()
        if ans == "Delhi":
            print("Congratulations,your answer is correct")
            points += 1
        else:
            print("Wrong answer")
            points -= 1
    elif choice == 2:
        print("who is the prime minister of America?")
        ans = input("enter your ans: ").capitalize()
        if ans == "Joe":
            print("Congratulations,your answer is correct")
            points += 1
        else:
            print("Wrong answer")
            points -= 1
    elif choice == 3:
        print("your any question..")
        ans3 = input("enter your answer: ").capitalize()
        if ans3 == "Answer here":
            print("Congratulations,your answer is correct")
            points += 1
        else:
            print("wrong answer")
            points -= 1
    elif choice == 0:
        print("Your total point is {}".format(points))
        break
    else:
        print("No such option.")
        print("Points: {}".format(points))
        break