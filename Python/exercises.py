import random
import string


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
#
# # 1
#
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
#
#
# DB exercises

# 1

# price = {"Burger": 4.50, "Hotdog": 3.50}  # created a dictionary so the item price variable can be established
# user_funds = 10.31
# item_price = price["Burger"]  # there is no definition for price - from the format of the variable it's visible that
# # it's a dictionary type data
#
# if item_price < user_funds:
#     print("You have enough money!")  # syntax error - fix - change Print - print
# elif item_price == user_funds:  # syntax error - fix - change = to ==, changed if to elif
#     print("You have the precise amount of money")
# elif item_price < user_funds:  # changed if to elif
#     print("Sorry you don't have enough money")  # fix - added speach marks at the start and end of the string

# 2

# def product(n):
#     total = 1  # syntax error - fix - '==' to '='
#     for i in n:  # name error - fix - change the first 'n' to 'i'
#         total *= i
#     return total  # corrected indentation
#
#
# print(product([4, 4, 5]))

# 3

# def is_prime(x):
#     if x < 2:
#         return False
#     else:
#         for n in range(2, x - 1):
#             if x % n == 0:  # syntax fix - '=' to '=='
#                 return False
#             else:
#                 return True
#
#
# print(is_prime(2))
# print(is_prime(3))
# print(is_prime(4))
# print(is_prime(5))
# print(is_prime(6))
# print(is_prime(7))
# print(is_prime(15))
# print(is_prime(20))
# print(is_prime(25))

# academia.edu ex

# Anagram Checker

# def AnagramChecker(x, y):
#     word1_list = sorted([*x.lower().replace(' ', '')])
#     word2_list = sorted([*y.lower().replace(' ', '')])
#
#     if word1_list == word2_list:
#         return print("These two strings are an anagram")
#     else:
#         return print("These two strings are not an anagram")
#
#
# if __name__ == '__main__':
#     word1 = input("Enter your first string: ")
#     word2 = input("Enter your second string: ")
#
#     AnagramChecker(word1, word2)
#

# Pass Generator
def PasswordGenerator():
    pass_length = 30

    password = ""

    while pass_length > 0:
        pass_gen = str(random.choice(string.ascii_letters + string.punctuation + string.digits))
        password += pass_gen
        pass_length -= 1
    return password


print(PasswordGenerator())
