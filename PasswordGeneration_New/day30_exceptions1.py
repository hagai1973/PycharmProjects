# a_dictionary = {"name": "hagai"}
# value = a_dictionary["name"]
# print(f"name is: {value}")

# with open("data.txt", 'r') as file:
#     print(file.read())
#
#
# fruit_list = ["apple", "orange", "bannana"]
# print(fruit_list[1])
#
# for a in fruit_list:
#     print(f"*** {a}")

try:
    file = open("data2.txt")
    my_dic = {"key": "454545454"}
    print(my_dic["key"])
except FileNotFoundError:
    # print("there is a problem")
    file = open("data2.txt", "w")
    file.write("dfdfdfdfd")
except KeyError as err_msg:
    print(f"{err_msg} key does not exist")
except NameError:
    print("key does not exist 2")
else:
    print(file.read())
finally:
        file.close()
        print("file closed")
        raise TypeError("my error")