# name = "Angela"
# letters = [letter for letter in name]
# print(letters)

# new_list = [n * 2 for n in range(1, 5)]
# print(new_list)


# names = ["Alex", "Beth", "Carolina", "Dave", "Eleanor", "Freddie"]
# new_name = [name.upper() for name in names if len(name) > 5]
# print(new_name)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# new_list_unite = [number * number for number in numbers]
# new_list2 = [(number ** 2) for number in numbers]
# print(new_list_unite)
# print(new_list2)
# new_list_unite = [number for number in numbers if number % 2 == 0]
# print(new_list_unite)

# my_file = open("file1.txt", "r")
# content = my_file.read()
# print(content)
# content_list = (content.split())
# my_file.close()
# print(content_list)

with open("file1.txt", "r") as file1:
    content_list1 = file1.readlines()

with open("file2.txt", "r") as file2:
    content_list2 = file2.readlines()

# Convert string to int in lists
# file1_list = content_list1
# file2_list = content_list2
print(content_list1)
print(content_list2)

#  Syntax
# new_list = [new_item for item in items if condition]
new_list_unite = [int(number) for number in content_list1 if number in content_list2]
print(new_list_unite)
