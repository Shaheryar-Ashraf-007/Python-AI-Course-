# #write a program to check the even number in the list 
# numbers = int(input("Enter your number:"))

# if (numbers % 2==0):
#     print(f"it is even number",numbers)
# else:
#     print = input("it is not a event number")
# #check is a string is palindrome 

# a = input("Enter a word:")
# rev = a[::-1]
# if a == rev :
#     print(f"it is palindrome",rev)
# else:
#     print(f"it is not a palindrome")
# #write a program to remove the duplicates 

# def remove_duplicates(input_list):
#     unique_list = set(input_list)
#     unique_list = list(unique_list)
#     return(unique_list)
# original_list = [1,2,2,2,3,4,5,6,6,6,6,7,8,8,8,8,9]
# result_list = remove_duplicates(original_list)
# print(f"original_list",original_list)
# print(f"result with remove duplicates", result_list)

# #create  program to ceck the specific element exist

# my_list = int(input("Enter a number list"))

# check_element = int(input("Enter specific element to check :"))
# if check_element in my_list:
#     print(f"yes it is present",check_element)
# else:
#     print(f" it is not present")
    
# #write a prigram to calculate the vowels in the list 
# sentence = input("Enter a sentence:")
# l = ("a","e","i","o","u")
# count = 0
# for char in l :
#     if char in l :
#         count +=1
#         print(count)
# #calculate the number is prime or not
# num = int(input ("Enter a number:"))
# if num == 0 :
#     print(f"it is not a prime number")
# if num > 0:
#     for i in range(2,num):
#         if (num % i ==0):
#             print(f"{num}, it is not a prime number")
#         break 
#     else:
#         print(f"it is prime number")
# #calculte the factorial of number

# def factorial(n):
#     if n==1 or n==0 :
#         return n==1
#     else:
#         return n * factorial(n-1)
# number = int("Enter a number:")
# result = factorial(number)
# print(f" the factorial of number is :", result)

# import random
# while True:
#     print("""
#         ~~~~~~~~~~~~~~~Welcome to RPS~~~~~~~~~~~~~""")
#     name = input("Enter your Name:")
#     user_score = 0
#     comp_score = 0
#     Tie = 0
#     print("""
#         Wining rules:
#         1.Rock vs Paper--->Paper
#         2.Scissor vs Rock---> Rock
#         3.Paper vs Scissor--->Scissor""")
#     print("""
#         Choices are :
#         1.Rock
#         2. Paper
#         3.Scissor""")
#     print()
#     user_choice = int(input("Enter a Choice:"))
#     while user_choice >3 or user_choice < 1 :
#         user_choice = input("Enter a Valid Choice")
#     if user_choice == 1:
#         user_choice = "Rock"
#     elif user_choice == 2:
#         user_choice = "Paper"
#     else:
#         user_choice = "Scissor"
#         print(f"the user choice is:", user_choice)
#         print(f"Now it's Computer Turn:")
#     computer = random.randint(1,3)
#     if computer == 1:
#         computer_choice = "Rock"
#     elif computer ==2:
#         computer_choice = "Paper"
#     else:
#         computer_choice = "Scissor"
#         print(f"The computer choice is:", computer_choice)
#     if ((user_choice == "Rock" and computer_choice == "Paper") or user_choice =="Paper" or user_choice == "Rock"):
#         print("Paper Wins")
#         result = "Paper"
#     elif ((user_choice == "Scissor" and computer_choice == "Rock") or user_choice =="Rock" or user_choice == "Scissor"):
#         print("Rock Wins")
#         result = "Rock"
#     elif computer_choice == user_choice:
#         print("it is tie")
#         result = "Tie"
#     else:
#         print("Rock Wins")
#         result = "Rock Wins"
#     if result == "Tie":
#         ties =+1
#     elif result == user_choice: 
#         print("user wins")
#         user_score =+1
#     else:
#         comp_score=+1
#         print("computer Wins")
#     print("Scores are:")
#     print(name, "'s user_score", user_score)
#     print("Computer score is:", comp_score)
#     print("Scores are ties", ties)
#     repeat = input("Do you want to play again?")
#     if repeat == "No" or repeat == "No":
#         break
#     print("Game Over")
#     print("Thanks for Watching")
    
    
    
    
# #tupple 
# userNames = print ("shery", "moon")


fullName = "shahaeryar     ashraf"
FullName = fullName.lower()
userName = "NAVEED SARVAR"
print = (userName[0:6:2])  
fullName = fullName.lstrip(userName)
userName = fullName.index("s")
userName = fullName.replace("ashraf","shaheryar")
fullName = "shaheryar"
lowerFullName = fullName.split(",")
print(lowerFullName)
fullName = "shaheryar"
lowerFullName = fullName.startswith("sfd")
print(lowerFullName)
fullName = "shaheryar"
lowerFullName = fullName.isdigit()
print(lowerFullName)
print(fullName)
tableString = f"table row:2*{index} = {total}"



  

    
    
    