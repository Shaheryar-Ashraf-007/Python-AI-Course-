# #calculate your age based on current year and birth year 

birth_year = input("Enter you bitrh_year:")

current_year = input("Enter your current_year:")

year = int(current_year) - int(birth_year)

current_age = (year)

print("Your Current Age Is")

print = input(current_age)

# # calculate the area of rectangle 

lenght= input("Enter your lenght:")

width = input("Enter your width:")

area = int(lenght)*int(width)

Current_area = (area)

print = input(Current_area)

# # calculate the area of circle 
import math 

radius = float(input("Enter the radius:"))

area_of_circle = math.pi*radius**2

if(radius < 0):
    
    print = input("radius can not be nagetive")
    
else:
    
    print = input(area_of_circle)
    
# #calculate the area of cube 

side = float(input("Enter the side of the cube:"))

area_of_cube = 6*int(side)**2
if(side < 0):
    print = input("area cannot be nagetive")

print = input(area_of_cube)

# change the temp faranhite to celcius 

temp_farahniehite = float(input("Enter Tempreture in Farahniehite:"))

celcius_tempt = (temp_farahniehite - 32) *5/9

print = input(celcius_tempt)

# #convert the number into minutes and seconds

num = int(input("Enter a number which changes into minutes:"))

num2 = int(input("Enter a number which changes into seconds:"))

change_in_minute = (num)/60

change_in_seconds = (num2)/3600

print = input(change_in_minute)

print = input(change_in_seconds)

# Write a program that calculates the percentage 

sub1 = float(input("Enter the marks of English:"))

sub2 = float(input("Enter the marks of Maths:"))

sub3 = float(input("Enter the marks of Chemistry:"))

sub4 = float(input("Enter the marks of Biology:"))

sub5 = float(input("Enter the marks of Urdu:"))

total = sub1 + sub2 + sub3 + sub4 +sub5

percentage = (total)/500*100

print = str("Your Total Marks in percentage:")

print = input (percentage)

#convert days into weeks

days = int(input("Enter number of days that you convert into weeks:"))

print = str("days in weeks")

weeks = int (days%365)/7

print = str("days in days")

d = int(days%365)%7 

print(weeks,"\n",d)

















