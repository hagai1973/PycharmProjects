


# write to a file
with open(file="/Users/hagai.tregerman/OneDrive - Forcepoint/Desktop/my_file.txt", mode="w") as file:  # create new file
    file.write("\n this is a new text")
    # append to a file
# with open(file="my_file_1.txt", mode="a") as file:  # create new file
#     file.write("\n this is a new text")


# Get content of file
file = open("my_file_1.txt")
content = file.read()
print(content)
file.close()