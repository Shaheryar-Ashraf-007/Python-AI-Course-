import random
while True:
    print("""
        ~~~~~~~~~~~~Welcome to RPS ~~~~~~~~~~~~~~""")
    name = input("Enter your Name:")
    user_score = 0
    Tie = 0
    comp_score = 0
    print("""
        Wining Rules :
        1. Rock vs Paper--->Paper
        2. Scissor  vs Paper --->Scissor
        3. Rock vs Scissor -->Rock""")
    print("""
        Choices are
        1. Rock 
        2. Paper
        3. Scissor""")
    print()
    user_choice = int(input("Enter your choice from 1-3:"))
    print()
    while user_choice > 3 or user_choice < 1:
        user_choice = int(input("Enter a Valid Input:"))
    if user_choice == 1:
        user_choice = "Rock"
    elif user_choice == 2:
        user_choice = "Paper"
    else:
        user_choice == "3"
        user_choice = "Scissor"
        
    print(f"The user choice is :", user_choice)
    print(f"Now it is Computer's Turn")
        
    computer = random.randint(1,3)
    if computer == 1:
        computer_choice = "Rock"
    elif computer == 2:
        computer_choice = "Paper"
    else:
        computer = 3
        computer_choice = "Scissor"
    print(f"computer choice is:", computer_choice)
        
    if ((user_choice == "Rock" and computer_choice == "Paper") or user_choice == "Paper" and user_choice == "Rock"):
        print("Paper Wins")
        result = "Paper"
    elif ((user_choice == "Paper" and computer_choice == "Scissor") or user_choice == "Scissor" and user_choice == "Paper"):
        print("Scissor wins ")
        result = "Scissor"
    elif computer_choice == user_choice :
        print("It is Tie")
        result = "Tie"
    else:
        print("Rock Wins")
        result = "Rock Wins"
    if result == "Tie":
        ties =+1
    elif result == "user_choice":
        user_score +=1
        print("user wins")
    else:
        comp_score+=1
        print("computer wins")
        print("Scores are")
        print(name,"'s user_score is: ", user_score)
        print("comp_score is:", comp_score)
        print("ties is", Tie)
        
        repeat = input("Do you want to play again?")
        if repeat == "No" or repeat == "No":
            break
        print("Game Over")
        print("Thanks for Watching")
        
import random
while True:
    print("""
        ~~~~~~~~~~~~~~~~~~Welcome to RPS ~~~~~~~~~~~~~~~~~""")
    Tie = 0
    user_score =0
    comp_score = 0
    name = input("Enter your name:")
    print("""
        Wining Rules:
        1. Rock vs Paper--->Paper
        2. Scissor vs Papper---> Paper
        3. Scissor vs Rock--->Rock""")
    print("""
        Choices are:
        1. Rock
        2.Paper
        3.Scissor""")
    print()
    user_choice = int(input("Enter your choice:"))
    print()
    while user_choice > 3 or user_choice < 1:
        user_choice = int(input("Enter a Valid Number:"))
    if user_choice == 1:
        user_choice = "Rock"
    elif user_choice == 2:
        user_choice = "Paper"
    else:
        user_choice == "3"
        user_choice = "Scissor"
    print(f"This is User choice", user_choice)
    print(f"Now it is Computer's Turn")
    computer = random.randint(1,3)
    if computer == 1:
        computer_choice = "Rock"
    elif computer ==2:
        computer_choice = "Paper"
    else:
        computer =="3"
        computer_choice = "Scissor"
    print("This is computer's choice", computer_choice)

    if ((user_choice == "Rock" and computer_choice == "Paper") or user_choice == "Paper" and computer_choice == "Rock"):
        print("Paper Wins")
        result = "Paper"
    elif ((user_choice == "paper" and computer_choice == "Scissor") or user_choice == "Scissor" and computer_choice == "Paper"):
        print("Scissor Wins")
        result = "Scissor"
    elif computer_choice == user_choice:
        print("It is Tie")
        result = "Tie"
    else: 
        print("Rock wins")
        result = "Rock"
        
    if result == "Tie":
        ties =+1
    elif result == "user_choice":
        user_score =+1
        print("user wins")
    else:
        result == "computer_choice"
        comp_score=+1
        print("computer wins")
    print("Scores are:")
    print("it is ties",ties)
    print(name,"'s name is", user_score)
    print("It is computer's score",comp_score)
    repeat = input("Do you want to play againl?")
    if repeat == "No" or repeat == "NO":
        break
    print("Game Over")
    print("Thanks for playing")       