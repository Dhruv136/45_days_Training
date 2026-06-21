student ={
"name":"dhruv",
"class":"2nd year",
"rollno":"23",
"branch":"aids",
"address":"pilani",
"college":"BKBITS"
}
print(student)
print(student.keys())
print(student.items())
print(student["name"])
print(student["class"])
print(student["college"])
print(student["branch"])
print(student.get('nameq'))# if get function find a key then it print it otherwise return none
student.pop("name")
print(student)
student.popitem()

student.update({"class":"nigger"})
print(student)
new_student= student.copy() #create a shallow copy of student
print(new_student)

#  taking input from user then storing a dictionary

student = {}

name = input("Enter name: ")
age = input("Enter age: ")

student["name"] = name
student["age"] = age

print(student)