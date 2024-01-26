#write a program to check the even number in the list 
numbers = int(input("Enter your number:"))

if (numbers % 2==0):
    print(f"it is even number",numbers)
else:
    print = input("it is not a event number")
#check is a string is palindrome 

a = input("Enter a word:")
rev = a[::-1]
if a == rev :
    print(f"it is palindrome",rev)
else:
    print(f"it is not a palindrome")
#write a program to remove the duplicates 

def remove_duplicates(input_list):
    unique_list = set(input_list)
    unique_list = list(unique_list)
    return(unique_list)
original_list = [1,2,2,2,3,4,5,6,6,6,6,7,8,8,8,8,9]
result_list = remove_duplicates(original_list)
print(f"original_list",original_list)
print(f"result with remove duplicates", result_list)

#create  program to ceck the specific element exist

my_list = int(input("Enter a number list"))

check_element = int(input("Enter specific element to check :"))
if check_element in my_list:
    print(f"yes it is present",check_element)
else:
    print(f" it is not present")






    

