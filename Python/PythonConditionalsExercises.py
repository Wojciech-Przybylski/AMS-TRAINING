#Questions
question1 = "Answer the following sum. 4 + 4 = ? "
question2 = "Answer the following sum. 10 x 10 = ? "
question3 = "Answer the following sum. 54 / 6 = ? "
question4 = "Answer the following sum. 2^3 = ? "
question5 = "Answer the following question. What is the square root of 64? "
question6 = "Answer the following sum. 2 x 3 + 10 = ? "
question7 = "Answer the following sum. 50 / 5 - 10 = ? "
question8 = "Answer the following sum. 2(4+7)+3(2+2) = ? "
question9 = "Answer the following sum. 100^0 = ? "
question10 = "Answer the following sum. 2/3 + 4/3 = ? "

#Answers
answer1 = 8
answer2 = 100
answer3 = 9
answer4 = 8
answer5 = 8
answer6 = 16
answer7 = 0
answer8 = 34
answer9 = 0
answer10 = 2

score = []
percentage = 0

correct_answer = 10
incorrect_answer = 0


question1_input = input(question1)
question1_int = int(question1_input)

if question1_int == answer1:
    score.append(correct_answer)
else:
    score.append(incorrect_answer)

question2_input = input(question2)
question2_int = int(question2_input)

if question2_int == answer2:
    score.append(correct_answer)
else:
    score.append(incorrect_answer)

question3_input = input(question3)
question3_int = int(question3_input)

if question3_int == answer3:
    score.append(correct_answer)
else:
    score.append(incorrect_answer)

question4_input = input(question4)
question4_int = int(question4_input)

if question4_int == answer4:
    score.append(correct_answer)
else:
    score.append(incorrect_answer)

question5_input = input(question5)
question5_int = int(question5_input)

if question5_int == answer5:
    score.append(correct_answer)
else:
    score.append(incorrect_answer)#

question6_input = input(question6)
question6_int = int(question6_input)

if question6_int == answer6:
    score.append(correct_answer)
else:
    score.append(incorrect_answer)

question7_input = input(question7)
question7_int = int(question7_input)

if question7_int == answer7:
    score.append(correct_answer)
else:
    score.append(incorrect_answer)

question8_input = input(question8)
question8_int = int(question8_input)

if question8_int == answer8:
    score.append(correct_answer)
else:
    score.append(incorrect_answer)

question9_input = input(question9)
question9_int = int(question9_input)

if question9_int == answer9:
    score.append(correct_answer)
else:
    score.append(incorrect_answer)

question10_input = input(question10)
question10_int = int(question10_input)

if question10_int == answer10:
    score.append(correct_answer)
else:
    score.append(incorrect_answer)

for number in score:
    percentage += number

if percentage >= 90:
        print("Wowza! You scored an A in this test. You smashed it!")
elif percentage >= 70 <= 89:
        print("You did Great! You scored a B in this test")
elif percentage >= 50 <= 69:
        print("Well done you passed the test with a C!")
elif percentage >= 40 <= 49:
        print("Unfortunately you didn't pass the test, you scored a D, very close!")
elif percentage >= 30 <= 39:
        print("Not the best effort, you scored an E, you need to study more!")
else:
        print("You failed with a F grade, time to wake up!")
