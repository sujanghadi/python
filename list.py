subjects=["history","maths","geography","physics"]
for i in subjects:
	print(i)
# if you want to print index of value
for index, i in enumerate(subjects,start=1):
	print(index,i)

# convert our list into string
sub_str="_ ".join(subjects)
print(sub_str)

new_list=sub_str.split("_ ")
print(new_list)
print(subjects)