# from datetime import datetime
#
# now = datetime.now()
#
# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)

# new_dict = {new_key: new_value for (key, value) in dict.items() if test}
# import random
#
# names = ['Alex', 'Beti', 'Carolina', 'Dave', 'Eleanor', 'Freddie']
# student_score = {name: random.randint(1, 101) for name in names}
#
# print(student_score)
#
# student_score_passed = {name: grade for (name, grade) in student_score.items() if grade > 60}
# print(student_score_passed)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# words = sentence.split()
# print(words)
# words_dics = {word: len(word) for word in words}
# for key, value in words_dics.items():
#     print(key, ' : ', value)

weather_c ={
    "Monday": 12,
    "Thesday": 14,
    "Wednesday": 15
}

weather_f = {day: temp * 9/5 + 32 for (day, temp) in weather_c.items() }

weater_c_back = {day: ((temp - 32) * 5/9) for (day, temp) in weather_f.items()}

print(weather_f)
print(weater_c_back)