def factorial(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n * factorial(n-1)
# number = int(input("Enter a number:"))
# result = factorial(number)
# print = input(f"The factorial of number is {number}:{result}")

# #create a function to check the number is prime or not 

# number = int(input("Enter a Number:"))
# if number ==1:
#     print = input("it is not a prime number")
# if number>1:
#     for i in range(2,number):
#         if (number % i) == 0:
#             print = input(f"it is not a prime number")
#             break
#     else:
#         print = input(" it is a prime number")

# #define the function to find the sqaure of number 

# def sqaure(num):
#     return num**2
# num = int(input("Enter a number:"))
# result = sqaure(num)

# #write a function to calculate the reverse of string 

# def reverse_string(input_string):
#     return input_string[::-1]
# original_string = ("hello world")
# reversed_string = reverse_string(original_string)
# print = input(original_string)
# print = input(reversed_string)

# # Implement a function that counts the number of vowels in a given string.

# sentence = input("Eneter a sentence:")
# l = ("a","e","i","o","u")
# count = 0
# for char in sentence:
#     if char in l :
#         count +=1
#         print = input(count)
        
        
# #write the program to sum of element 


# my_list = [1,2,3,4,5,6]
# sum_of_element = sum(my_list)
# print = input(my_list)
# print = input(sum_of_element)

# #write a program to calculate the maximum and minimum number 

# numbers = [10,98,76,34]
# min_number = min(numbers)
# max_number = max(numbers)
# print = input(numbers)
# print = input(min_number)
# print = input(max_number)

# #calculate the specific element in list

# # Create a list
# my_list = [1, 2, 3, 4, 5]

# # Check if a specific element exists in the list
# element_to_check = 3

# if element_to_check in my_list:
#     print = input(f"{element_to_check} exists in the list.")
# else:
#     print = input(f"{element_to_check} does not exist in the list.")
    
# def remove_duplicates(input_list):
#     # Convert the list to a set to remove duplicates
#     unique_set = set(input_list)

#     # Convert the set back to a list
#     unique_list = list(unique_set)

#     return unique_list

# # Test the function
# original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
# result_list = remove_duplicates(original_list)

# print(f"Original List:", original_list)
# print(f"List with Duplicates Removed:", result_list)


# # Existing list
# original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # List comprehension to create a new list with even numbers
# even_numbers_list = [num for num in original_list if num % 2 == 0]

# # Print the result
# print(f"Original List:", original_list)
# print(f"Even Numbers List:", even_numbers_list)




# #write a program to check that string is palindrome or not 

# a = input("Enter a word:")

# rev =a[::-1]
# if a == rev:
#     print =input("it is palindrome")
# else:
#     print = input("it is not a palindrome")