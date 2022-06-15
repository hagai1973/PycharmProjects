import csv
import pandas

#
# with open('weather_data.csv', newline='') as data_file:
#     reader = csv.reader(data_file)
#     data = list(reader)
#
# temperatures = []
# for line in data[1:]:
#     # print (line[1])
#     temperatures.append(int(line[1]))
#
# print (temperatures)

data = pandas.read_csv("weather_data.csv")
# print(data.condition)
# print(data[data.condition == "Sunny"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# converted = ((int(monday.temp) * 9) / 5) + 32
# print(f"Fahrenheit: {monday.temp}")
# print(f"Celsius: {round(converted, 2)}")
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
#
# print(temp_list)
# total_temp = 0
# for temp in temp_list:
#     total_temp += temp
#
# avg_temp = total_temp/len(temp_list)
# average = data["temp"].mean()
# max_temp = data["temp"].max()
# print(f"Average temp is: {round(avg_temp,2)}")
# print(f"Average temp is: {average}")
# print(f"max temp is: {max_temp}")


# print(type(data))
# print(type(data["temp"]))

data_dic = {
    "student": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dic)
print(data)
data.to_csv("grades.csv")