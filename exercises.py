# Qa exercise
# for i in range(5):
#   name = input("What is your name?")
#  count = 0
# while count < 5:
#    print(name, "is awesome!")
#   count += 1

# w3resource exercises

# 1
#ex1_list = []
#for i in range(2701)[1500:2701]:
 #   if i % 7 == 0 and i % 5 == 0:
  #      ex1_list.append(i)
#print(ex1_list)

# 2
input_stage = int(input(f"choose temperature conversion:"
                    f"\n1. Celsius"
                    f"\n2. Fahrenheit"
                    f"\n"))
if input_stage == 1:
    celsius_conv = input("Enter temperature in Celsius: ")
    fahrenheit_output = (int(celsius_conv)*9/5) + 32
    print(f"{fahrenheit_output} F")
elif input_stage == 2:
    fahrenheit_conv = input("Enter temperature in Fahrenheit: ")
    celsius_output = (int(fahrenheit_conv) - 32)*5/9
    print(f"{celsius_output} C")


