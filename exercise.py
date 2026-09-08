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

# WAP to swap two numbers using a third variable