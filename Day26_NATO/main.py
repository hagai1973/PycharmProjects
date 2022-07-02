# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
name = input('What is your name?\n').upper()
# Split the letter in the Name
list_letters = list(name)

# Get list of letters with NATO value
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

# nato_data_dict = {}
# list_of_nato_from_name = []

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
# for (index, row) in nato_data_frame.iterrows():
#     # print(f"{row.letter}: {row.code}")
#     nato_data_dict[row.letter] = row.code

nato_data_dict_new = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
output_list = [nato_data_dict_new[letter] for letter in name]

print(output_list)
# for letter in list_letters:
#     for (key, value) in nato_data_dict_new.items():
#         # print(key)
#         # print(value)
#         if key == letter.upper():
#             list_of_nato_from_name.append(value)

# print("Your NATO name is: " + str(list_of_nato_from_name))


