# Qa exercise
# for i in range(5):
#   name = input("What is your name?")
#  count = 0
# while count < 5:
#    print(name, "is awesome!")
#   count += 1


# w3resource exercises

# 1
# ex1_list = []
# for i in range(2701)[1500:2701]:
#    if i % 7 == 0 and i % 5 == 0:
#        ex1_list.append(i)
# print(ex1_list)

# 2
# input_stage = int(input(f"choose temperature conversion:"
#                    f"\n1. Celsius"
#                    f"\n2. Fahrenheit"
#                    f"\n"))
# if input_stage == 1:
#    celsius_conv = input("Enter temperature in Celsius: ")
#    fahrenheit_output = (int(celsius_conv)*9/5) + 32
#    print(f"{fahrenheit_output} F")
# elif input_stage == 2:
#    fahrenheit_conv = input("Enter temperature in Fahrenheit: ")
#    celsius_output = (int(fahrenheit_conv) - 32)*5/9
#    print(f"{celsius_output} C")
#
# Functions (QA)
#
# def add_calc(number1, number2):
#    answer = number1 + number2
#    return answer
#
#
# added_number = add_calc(5, 5)
# print(added_number + 20)

# 1

# def grade_calc(hm, assessment, exam):
#     total_score = int(hm) + int(assessment) + int(exam)
#     grade_percentage = (total_score / 175) * 100
#     return grade_percentage
#
#
# student_name = input("Enter your name here: ")
#
# homework_score = input("Enter your homework score (/25): ")
#
# assessment_score = input("Enter your assessment score (/50): ")
#
# exam_score = input("Enter your exam score (/100): ")
#
# print(
#     f"Here is your percentage score "
#     f"\nStudent: {student_name} "
#     f"\nPercentage: "
#     f"{'%.0f' % grade_calc(homework_score, assessment_score, exam_score)}%")


