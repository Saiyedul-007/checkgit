# # WAP to print "Hello, World! on the screen"
# print("Hello, World!")

# # WAP to read two numbers and print their sum
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# print(f"The sum of {num1} and {num2} is {num1 + num2}")

# WAP to read two numbers and print their sum, difference, product and quotient.
first_num = float(input("Enter number: "))
second_num = float(input("Enter number: "))
operator = input("Enter the operator: ") # Take the operator to do the specific operation

match operator:
    case "+": # Addition
        print(f"The sum of {first_num} and {second_num} is {first_num + second_num}")
    case "-":
        print(f"The difference of {first_num} and {second_num} is {first_num - second_num}")
    case "*":
        print(f"The product of {first_num} and {second_num} is {first_num * second_num}")
    case "/":
        print(f"The quotient of {first_num} and {second_num} is {first_num / second_num}")
    case _:
        print("Invalid operator.")


