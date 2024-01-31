# students = {
#     "id":1,
#     "email": "student1@gmail.com",
#     "roll no": 34354,
#     "class": "WMA"
# },
# {
#     "id": 2,
#     "email": "student2@gmail.com",
#     "roll no ": 343545,
#     "class": "WMA"
# },
# {
#     "id": 3,
#     "email": "student3@gmail.com",
#     "roll no ": 343786,
#     "class": "WMA"
# },
# {
#     "id": 4,
#     "email": "student4@gmail.com",
#     "roll no ": 3433446,
#     "class": "WMA"
# },
# {
#     "id": 5,
#     "email": "student5@gmail.com",
#     "roll no ": 3487765,
#     "class": "WMA"
# },

# #CURRENT VALUES 
# students = [{
#     "id":1,
#     "email": "student1@gmail.com",
#     "roll no": 34354,
#     "class": "WMA"
    
# },
            
# { 
#     "id":2,
#     "email": "student2@gmail.com",
#     "roll no": 34354,
#     "class": "WMA"
# },
# {
#     "id":3,
#     "email": "student3@gmail.com",
#     "roll no": 34354,
#     "class": "WMA"
# },
# {
#     "id":4,
#     "email": "student4@gmail.com",
#     "roll no": 34354,
#     "class": "WMA"
# },
# {
#     "id":5,
#     "email": "student5@gmail.com",
#     "roll no": 34354,
#     "class": "WMA"
# },
   
            
#             ]

# email = input("please enter your email")
# newStudent = {
#     "id": len(students)+1,
#     "id":1,
#     "email": "student1@gmail.com",
#     "roll no": 34354,
#     "class": "WMA"
    
# students.append(newStudent)
# update_id = int(input ("enter your id"))
# updatedEmail = input("please enter yuor enmail")

# def updateStudent(student):
#     if student["id"] == update_id:
#         return
# {
#         "id": len(students)+1,
#         "id":1,
#         "email": "student1@gmail.com",
#         "roll no": 34354,
#         "class": "WMA"
#         }
# else:
#     student

# students = list(map(updateStudent,students))
# #delete any studenys
# def deleteStudent(student): 
# students = list(filter())
#Student APP 

students = [{
    "id" : "1",
    "name": "ali",
    "email": "ali1@gmail.com",
    "roll no ": 2345,
    "class": "py",
           
},
{
    "id" : "2",
    "name": "hassan",
    "email": "hassan2@gmail.com",
    "roll no ": 23456,
    "class": "WMA",
},
{
    "id" : "3",
    "name": "hussain",
    "email": "hussain3@gmail.com",
    "roll no ": 23678,
    "class": "genrative AI",
},
{
    "id" : "4",
    "name": "Shery",
    "email": "shery4@gmail.com",
    "roll no ": 23123,
    "class": "Graphic designing",
},
{
    "id" : "5",
    "name": "moon",
    "email": "moon5@gmail.com",
    "roll no ": 24567,
    "class": "video annimation",
},
            ]
email = input("Enter your email:")
newStudent = {
    "id" : str(len(students)+1),
    "name": "yahya",
    "email": "yahya6@gmail.com",
    "roll no ": 6733,
    "class": "CISCO",
    
}
students.append(newStudent)
for student in students:
    print("Students email:"+ student["email"] , "id:",student["id"])
update_id = int(input("Enter your id :"))
updatedEmail = (input("Enter your email:"))
def updateStudent (student):
    if student["id"] == update_id:
        return{
            "id" : student["id:"],
            "name": student["name:"],
            "email": student["email:"],
            "roll no ": student["roll no:"],
            "class": student["class"],
         }
    else:
        return student
student = list(map(updateStudent,students))
print("students", student)
id = int(input("delete required students:"))
def deleteStudent(student):
    if student["id "] != update_id:
        return student
    students = list(filter(deleteStudent, students))
for student in students:
    print("Student Email:"+student["email"],"id:", student["id"])

        


 
        
    



