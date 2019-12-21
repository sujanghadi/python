#dictionaries ..allows key value pair
#key is unique identifier where we find our data and value is that data

student={"name":"sujan","age":29,"courses":["math","comp"]}
print(student)
print(student["age"])
print(student["courses"])

#if we want to access the key which doesent exit in dict 

print(student.get("phone","key not found"))
#adding new entry to dictionary

student={"name":"sujan","age":29,"courses":["math","comp"]}
student["phone"]="9421266954"
print(student.get("phone"))

#update the values
student["name"]="kiran"
print(student)

student.update({"name":"pallavi","age":32,"phone":"9975947604"})
print(student)

del student["age"]
print(student)


print(student.values())