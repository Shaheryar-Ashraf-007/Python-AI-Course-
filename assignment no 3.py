# #sum of two variables
NUM1 = 645
NUM2 = 7565
print(NUM1+NUM2)


#  #Swap the values of two variables without using a temporary variable.
 
myValue = 5645
print("your myValue is :")
yourValue = 4342
myValue, yourValue = yourValue, myValue
print("your yourValue is : ")
print(myValue,"\n",yourValue)


# #  Calculate the area of a rectangle using user input for length and width.


lenght= input("Enter your lenght:")

width = input("Enter your width:")

area = int(lenght)*int(width)

Current_area = (area)

print = input(Current_area)

#convert tempt celcius to faranhite 

temp_Celcius = float(input("Enter Tempreture in Celcius:"))

Farahniehite_tempt = temp_Celcius*(5/9)+32 

print = input(Farahniehite_tempt)

# # Create a program that takes user input for the radius and calculates the area of a circle.

import math 

radius = float(input("Enter the radius:"))

area_of_circle = math.pi*radius**2

if(radius < 0):
    
    print = input("radius can not be nagetive")
    
else:
    
    print = input(area_of_circle)

# #check if number is positive or negetive 
# Get input from the user
number = int(input("Enter a number:"))
if number > 0 :
    print = input ("Your number is postive")
elif number < 0:
    print = input (" your number is negetive")
else:
    print = input (" your number is equal to zero")
    
# #determine if this year is a leap year 

year =int(input("Enter year:"))
if (year%4==0 and year % 100!=0) or (year % 400 ==0):
    print = input("year is a leap year")
else:
    print = input("year is not a leap year")
    
#check number is a even or odd 

Num = int(input("Enter a number:"))

if (Num % 2 == 0):
    print = input("your number is even")
else:
    print = input("your number is odd")  

#compare three numbers and find out the largest number 
a = int(input("Enter a first number:"))
b = int(input("Enter Second number:"))
c = int(input("Enter third number:"))
if a>=b and a>=c :
    print = input("your first number is largest")
elif b>=a and b>=c :
    print = input("your second number is largest")
elif a==b==c:
    print = input("your all number is equal")
else:
    print = input("your third numbr is largest")

#implement calculator 

a = int(input("enter first number:"))
operator = input("enter operator(+,-,*,/) :")
b = int(input("Enter second number:"))
result = 0
if operator == "+":
    result = a+b
elif operator == "-":
    result = a-b
elif operator =="*":
    result =a*b
elif operator == "/":
    result = a/b
if a!=0:
    result = a/b
else:
     print = input("Error: Invalid operator.")
     exit()
print = input(f"the result of {a} {operator} {b} is: {result}")

#calculate the factorial of a number 

def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n * factorial(n-1)
number = int(input("Enter a number:"))
result = factorial(number)
print = input(f"The factorial of number is {number}:{result}")

#create a function to check the number is prime or not 

number = int(input("Enter a Number:"))
if number ==1:
    print = input("it is not a prime number")
if number>1:
    for i in range(2,number):
        if (number % i) == 0:
            print = input(f"it is not a prime number")
            break
    else:
        print = input(" it is a prime number")

#define the function to find the sqaure of number 

def sqaure(num):
    return num**2
num = int(input("Enter a number:"))
result = sqaure(num)

#write a function to calculate the reverse of string 

def reverse_string(input_string):
    return input_string[::-1]
original_string =input("Enter your word that you want to reverse the string")
reversed_string = reverse_string(original_string)
print = input(original_string)
print = input(reversed_string)

# Implement a function that counts the number of vowels in a given string.

sentence = input("Eneter a sentence:")
l = ("a","e","i","o","u")
count = 0
for char in sentence:
    if char in l :
        count +=1
        print = input(count)
        
        
#write the program to sum of element 


my_list = [1,2,3,4,5,6]
sum_of_element = sum(my_list)
print = input(my_list)
print = input(sum_of_element)

#write a program to calculate the maximum and minimum number 

numbers = [10,98,76,34]
min_number = min(numbers)
max_number = max(numbers)
print = input(numbers)
print = input(min_number)
print = input(max_number)

#calculate the specific element in list

# Create a list
my_list = [1, 2, 3, 4, 5]

# Check if a specific element exists in the list
element_to_check = 3

if element_to_check in my_list:
    print = input(f"{element_to_check} exists in the list.")
else:
    print = input(f"{element_to_check} does not exist in the list.")
    
def remove_duplicates(input_list):
    # Convert the list to a set to remove duplicates
    unique_set = set(input_list)

    # Convert the set back to a list
    unique_list = list(unique_set)

    return unique_list

# Test the function
original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
result_list = remove_duplicates(original_list)

print(f"Original List:", original_list)
print(f"List with Duplicates Removed:", result_list)


# Existing list
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension to create a new list with even numbers
even_numbers_list = [num for num in original_list if num % 2 == 0]

# Print the result
print(f"Original List:", original_list)
print(f"Even Numbers List:", even_numbers_list)




#write a program to check that string is palindrome or not 

a = input("Enter a word:")

rev =a[::-1]
if a == rev:
    print =input("it is palindrome")
else:
    print = input("it is not a palindrome")
    
    
    ##create a game of stone paper seecor 

import random
while True:

    print("~~~~~~~~~~~~Welcome to RPS~~~~~~~~~~~~")

    user_score = 0
    comp_score = 0
    ties = 0

    name = input(" Enter your Name here:")
    print("""
        wining rules:
        1. Paper vs Rock --->Paper
        2. Rock vs Scissor --->Rock
        3. Scissor vs Paper --->Scissor""")

    print(""" 
        Choices are:
        1. Rock 
        2. Paper
        3. Scissor
        """)
    print()
    user_choice = int(input("Enter your Choices from 1-3:"))
    print()
    while user_choice >3 or user_choice <1:
        user_choice = int(input("Enter a valid input:"))
        
    if user_choice == 1:
        user_choice = "Rock"
    elif user_choice == 2:
        user_choice = "Paper"
    else:
        user_choice == "3"
        user_choice = "Scissor"

    print(f"the user_choice is:", user_choice)
    print (f"Now it is Computer's Turn:")

    computer = random.randint(1,3)
    if computer ==1:
        computer_choice = "Rock"
    elif computer ==2:
        computer_choice = "Paper"
    else:
        computer = 3
        computer_choice = "Scissor"
    print(f"the computer's choice is :", computer_choice)

    if ((user_choice == "Paper" and computer_choice == "Rock") or user_choice == "Rock" and computer_choice =="Paper"):
        print("Paper Wins")
        result = "Paper"
    elif ((user_choice == "Scissor" and computer_choice == "Rock") or user_choice == "Rock" and computer_choice == "Scissor" ):
        print("Rock Wins")
        result = "Rock"
    elif  user_choice == computer_choice:
            print("it is tie")
            result = "Tie"
            
    else:
        print("Scissor Wins")
        result = "Scissor"
        
    if result == "Tie":
        ties =+1  
    elif result == user_choice:
        print("user Wins")
        user_score =+1
    else:
        computer_score=+1
        print("computer Wins")
    print("Scores are")
    print(name,"'s user_score is: ", user_score)
    print("comp_score is:", comp_score)
    print("ties is", ties)
    
    repeat = input("Do you want to play again?")
    if repeat == "No" or repeat == "No":
        break
    print("Game Over")
    print("Thanks for Watching")
    

