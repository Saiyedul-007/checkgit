# # WAP to print "Hello, World! on the screen"
# print("Hello, World!")

# # WAP to read two numbers and print their sum
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# print(f"The sum of {num1} and {num2} is {num1 + num2}")

# # WAP to read two numbers and print their sum, difference, product and quotient.
# first_num = float(input("Enter number: "))
# second_num = float(input("Enter number: "))
# operator = input("Enter the operator: ") # Take the operator to do the specific operation

# match operator:
#     case "+": # Addition
#         print(f"The sum of {first_num} and {second_num} is {first_num + second_num}")
#     case "-":
#         print(f"The difference of {first_num} and {second_num} is {first_num - second_num}")
#     case "*":
#         print(f"The product of {first_num} and {second_num} is {first_num * second_num}")
#     case "/":
#         print(f"The quotient of {first_num} and {second_num} is {first_num / second_num}")
#     case _:
#         print("Invalid operator.")


# # WAP to read the radius of a circle and print its area and circumference
# import math
# radius = float(input("Enter the radius of the circle: "))
# area = math.pi * radius ** 2
# circumference = 2 * math.pi * radius
# print(f"The area and circumference of the circle with radius {radius} unit are {area: .2f} sq. unit and {circumference: .2f} unit respectively.")

# # WAP to read the length and breadth of a rectangle and print its area and perimeter
# length = float(input("Enter the length of the rectangle: "))
# breadth = float(input("Enter the breadth of the rectangle: "))

# print(f"Area of the rectangle is: {length * breadth: .2f}")
# print(f"The perimeter of the rectangle: {2 * (length + breadth): .2f}")

# # WAP to swap two numbers using a third variable
# a = 6
# b = 7
# c = a
# a = b
# b = c
# print(a,b)

# WAP to swap two numbers without using a third variable
# Take two numbers as input
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# print(f"Before swapping: First = {num1}, Second = {num2}")

# # Swap without a third variable
# num1, num2 = num2, num1

# # Print the results
# print(f"After swapping: First = {num1}, Second = {num2}")

# WAP to read a temperature in Celsius and convert it to Fahrenheit
# celsius = float(input("Enter temperature in celsius: "))
# fahrenheit = celsius * (9/5) + 32
# print(f"The temperature {celsius} degree celsius is {fahrenheit: .2f} degree in Fahrenheit scale.")

# # WAP to read the marks of 5 subjects and print the total and average
# math = float(input("Enter the marks in Mathematics: "))
# biology = float(input("Enter the marks in Biology: "))
# english = float(input("Enter the marks in English: "))
# physics = float(input("Enter the marks in Physics: "))
# chemistry = float(input("Enter the marks in Chemistry: "))
# total_marks = math+biology+chemistry+physics+english
# average = total_marks / 5
# print("\n")
# print("STUDENT REPORT CARD".center(30,"-"))
# print(f"{'Mathematics'.ljust(20)} {math: .1f}")
# print(f"{'Biology'.ljust(20)} {biology: .1f}")
# print(f"{'English'.ljust(20)} {english: .1f}")
# print(f"{'Physics'.ljust(20)} {physics: .1f}")
# print(f"{'Chemistry'.ljust(20)} {chemistry: .1f}")
# print("*"*30)
# print(f"{'Total'.ljust(20)} {total_marks: .1f}")
# print(f"{'Average'.ljust(20)} {average: .1f}")

# # WAP to read seconds and convert them into hours, minutes and seconds
# second= int(input("Enter the amount of time in seconds: "))
# # minute = second // 60 # Convert the seconds into minute (total)
# # remaining_second = second % 60 # Calculate the seconds that remain after all conversions
# # hour = minute // 60 # Convert the total minutes into hours (total)
# # remaining_minute = minute % 60 # Calculate the minutes that remain after all conversions
# # print(f"For {second} in total: {hour} hour, {remaining_minute} minutes and {remaining_second} seconds passed")

# # A better way to do this
# total_minute, remaining_second = divmod(second, 60)
# hour, remainin_minute = divmod(total_minute, 60)

# print(f"{hour} hours, {remainin_minute} minutes, {remaining_second} seconds.")