import pandas

student_dict = {
    "students": ["bob", "max", "linda"],
    "score": [70, 80, 85]
}
#
# for (key, value) in student_dict.items():
#     # print(key)
#     print(value)

students_data_frame = pandas.DataFrame(student_dict)
# print(students_data_frame)
# for (key, value) in students_data_frame.items():
#     print(value)


for (index, row) in students_data_frame.iterrows():
    print(row.students)
    print(row.score)