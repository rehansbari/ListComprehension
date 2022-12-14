#Practicing list comprehension
#You can create a new list from an existing list as we have previously done using a for loop
#numbers = [1,2,3]
# new_list = []
# for n in list:
#     add_1 = n+1
# new_list.append(add_1)

#This is how list comprehension is done
# new_list = [new item for item in list] n = the expression, item = individual object in list that is iterable, list = original list
numbers = [1,2,3]
new_list = [n + 1 for n in numbers]
print(new_list)

name = "Rehan"
new_list2 = [letter for letter in name]

x = range(1,5)
double_x = [number*2 for number in x]
print(double_x)

#Conditional List Comprehension
# new_list = [new_item for item in list if <condition>]

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)