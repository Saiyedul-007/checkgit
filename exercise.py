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

# # WAP to read a number and check whether its even or odd
# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print(f"The number {number} is even")
# else:
#     print(f"The number {number} is odd.")

# # WAP to read three numbers and find the largest among them
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))

# if num1 > num2:
#     if num1 > num3:
#         print(f"In between {num1}, {num2} and {num3}, the first number {num1} is the greatest.")
#     else:
#         print(f"In between {num1}, {num2} and {num3}, the third number {num3} is the greatest.")
# else:
#     if num2 > num3:
#         print(f"In between {num1}, {num2} and {num3}, the second number {num2} is the greatest.")
#     else:
#         print(f"In between {num1}, {num2} and {num3}, the third number {num3} is the greatest.")

# # A better way (with conditionals)
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))

# # Check whether first number is the largest of the three
# if num1 > num2 and num1 > num3:
#     print(f"The first number {num1} is the largest.")
# # Check whether the second number is the largest of the three
# elif num2 > num1 and num2 > num3:
#     print(f"The second number {num2} is the largest.")
# # If both num1 and num2 are not the largest then only one choice remain
# else:
#     print(f"The third number {num3} is the largest.")

# ## The best way is to use max() function
# greatest = max(num1, num2, num3)
# print(f"The greatest number is {greatest}")

# #WAP to read three numbers and find the smallest among them
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
# # Check whether num1 is the smallest
# if num1 <= num3 and num1 <= num2:
#     print(f"The first number {num1} is the smallest.")
# elif num2 <= num3 and num2 <= num1:
#     print(f"The second number {num2} is the smallest.")
# else:
#     print(f"The third number {num3} is the smallest.")

# # WAP to read a year and check whether it is a leap year or not.
# year = int(input("Enter a year: "))
# # Check whether the year is divisible by 4
# if year % 4 ==0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"The year {year} is a leap year.")
#         else:
#             print(f"The year {year} is not a leap year.")
#     else:
#         print(f"The year {year} is not a leap year.")

# else:
#     print(f"The year {year} is not a leap year")

# # WAP to read a character and check whether it is a vowel or a consonant
# character = input("Enter a character: ").lower()
# # Check only for vowel cases
# match character:
#     case "a":
#         print(f"The character is a vowel.")
#     case "e":
#         print(f"The character is a vowel.")
#     case "i":
#         print("The character is a vowel.")
#     case "o":
#         print("The character is a vowel.")
#     case "u":
#         print("The character is a vowel.")
#     case _:
#         print("The character is a consonant.")

# # A better way:
# if character.isalpha() and len(character) == 1:
#     match character:
#         case "a"| "e"|"i"|"o"|"u":
#             print("The character is a vowel")
#         case _:
#             print("The character is a consonant.")
# else:
#     print("Invalid input. Please enter only one character.")

# # The best way:
# if character.isalpha() and len(character) == 1:
#     if character in "aeiou":
#         print("The character is a vowel.")
#     else:
#         print("The character is a consonant")
# else:
#     print("Invalid input. Please enter a single letter.")

# # WAP to read a character and check whether it is an alphabet, digit or special symbol
# character = input("Enter a character: ")
# # Check whether the character is single letter or not
# if len(character) == 1:
#     # Check whether the character is digit or alphabet
#     if character.isalnum():
#         if character.isalpha(): # Checking for alphabet
#             print(f"The character {character} is an alphabet.")
#         else: # Checking for digits
#             print(f"The character {character} is a digit.")
#     else: # Since not an alphabet or a digit, it has to be a special symbol.
#         print(f"The character {character} is a special symbol.")
# # Since not a single character the value is invalid
# else:
#     print("Invalid value. Please enter only a single character.")

# # A better way
# if len(character) == 1:
#     # Check whether the character is an alphabet
#     if character.isalpha():
#         print(f"The character {character} is an alphabet.")
#     # Check whether the character is a digit
#     elif character.isdigit():
#         print(f"The character {character} is a digit.")
#     else:
#         print(f"The character {character} is a special symbol.")
# else:
#     print("Invalid input. Please enter only one character.")

# # WAP to read the marks of a student and print the grade (A/B/C/D/Fail)
# mark = int(input("Enter the mark of the student: "))
# # check for the mark with the criteria given
# if mark >= 0 and mark <= 100:
#     if mark >= 90:
#         print("Grade A")
#     elif mark >= 80:
#         print("Grade B")
#     elif mark >= 60:
#         print("Grade C")
#     elif mark >= 40:
#         print("Grade D")
#     else:
#         print("Failed")
# else:
#     print("Invalid input. Please put within 0 to 100")

# # WAP to read a number and check whether it is divisible by both 3 and 5
# number = int(input("Enter a number: "))
# # Has to be divisible by both 3 and 5
# if number % 3 == 0 and number % 5 == 0:
#     print(f"The number {number} is divisible by both 3 and 5.")
# else:
#     print(f"The number {number} is not divisible by 3 or 5.")

# # WAP to read the age of a person and check whether they are eligible to vote
# age = input("Please enter your age: ")
# # The age has to be in an acceptable range
# if age.isdigit():
#     age = int(age)
#     if age >= 0 and age <= 100:
#         # The user is eligible to vote if he/she is 18 or above
#             if age >= 18:
#                 print("The user is eligible to vote.")
#             # The user is not yet eligible but very close to being eligible
#             elif age >= 16:
#                 print("The user is not yet eligible, please yet 1 or 2 years more.")
#             else:
#                 print("The user is not eligible to vote.")
# # The user has input invalid input
# else:
#     print("The user has given an invalid input. Please only use numbers for your age.")