# #sum of two variables
# NUM1 = 645
# NUM2 = 7565
# print(NUM1+NUM2)


#  #Swap the values of two variables without using a temporary variable.
 
# myValue = 5645
# print("your myValue is :")
# yourValue = 4342
# myValue, yourValue = yourValue, myValue
# print("your yourValue is : ")
# print(myValue,"\n",yourValue)


# #  Calculate the area of a rectangle using user input for length and width.


# lenght= input("Enter your lenght:")

# width = input("Enter your width:")

# area = int(lenght)*int(width)

# Current_area = (area)

# print = input(Current_area)

# #convert tempt celcius to faranhite 

# temp_Celcius = float(input("Enter Tempreture in Celcius:"))

# Farahniehite_tempt = temp_Celcius*(5/9)+32 

# print = input(Farahniehite_tempt)

# # Create a program that takes user input for the radius and calculates the area of a circle.

# import math 

# radius = float(input("Enter the radius:"))

# area_of_circle = math.pi*radius**2

# if(radius < 0):
    
#     print = input("radius can not be nagetive")
    
# else:
    
#     print = input(area_of_circle)

# #check if number is positive or negetive 
# # Get input from the user
# number = int(input("Enter a number:"))
# if number > 0 :
#     print = input ("Your number is postive")
# elif number < 0:
#     print = input (" your number is negetive")
# else:
#     print = input (" your number is equal to zero")
    
# #determine if this year is a leap year 

# year =int(input("Enter year:"))
# if (year%4==0 and year % 100!=0) or (year % 400 ==0):
#     print = input("year is a leap year")
# else:
#     print = input("year is not a leap year")
    
# #check number is a even or odd 

# Num = int(input("Enter a number:"))

# if (Num % 2 == 0):
#     print = input("your number is even")
# else:
#     print = input("your number is odd")  

# #compare three numbers and find out the largest number 
# a = int(input("Enter a first number:"))
# b = int(input("Enter Second number:"))
# c = int(input("Enter third number:"))
# if a>=b and a>=c :
#     print = input("your first number is largest")
# elif b>=a and b>=c :
#     print = input("your second number is largest")
# elif a==b==c:
#     print = input("your all number is equal")
# else:
#     print = input("your third numbr is largest")

# #implement calculator 

# a = int(input("enter first number:"))
# operator = input("enter operator(+,-,*,/) :")
# b = int(input("Enter second number:"))
# result = 0
# if operator == "+":
#     result = a+b
# elif operator == "-":
#     result = a-b
# elif operator =="*":
#     result =a*b
# elif operator == "/":
#     result = a/b
# if a!=0:
#     result = a/b
# else:
#      print = input("Error: Invalid operator.")
#      exit()
# print = input(f"the result of {a} {operator} {b} is: {result}")

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
original_string = ("hello world")
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


#write a program to check that string is palindrome or not 

a = input("Enter a word:")

rev =a[::-1]
if a == rev:
    print =input("it is palindrome")
else:
    print = input("it is not a palindrome")
    


    
        
    


       

    



 


