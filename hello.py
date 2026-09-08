# marks = int(input("Enter the marks of the student: "))
# attendance = int(input("Enter the attendance of the student: "))
# if marks >= 40 and attendance >= 75:
#     print("The student has passed the exam.")
# else:
#     print("The student has failed.")

# # WAP to check whether a number is positive, negative or zero
# input_number = float(input("Enter a number:"))
# if input_number > 0:
#     print(f"The number {input_number} is positive.")
# elif input_number < 0:
#     print(f"The number {input_number} is negative.")
# else:
#     print(f"The number {input_number} is zero.")

# # WAP to check and display that the number is even or odd
# number = int(input("Enter the number: "))
# if number % 2 == 0:
#     print(f"The number {number} is even.")
# else: 
#     print(f"The number {number} is odd.")

# # WAP to show the grades of the student
# mark = int(input("Enter the marks of the student: " ))
# if mark >= 90 and mark <= 100:
#     print("A grade")
# elif mark >= 80:
#     print("B grade")
# elif mark >= 60:
#     print("C grade")
# else:
#     print("Failed")

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))

# if num1 > num2:
#     # If we are inside this block, we know num1 beat num2. 
#     # Now we just need to test num1 against num3.
#     if num1 > num3:
#         print(f"The first number: {num1} is the greatest of the three.")
#     else:
#         print(f"The third number: {num3} is the greatest of the three.")
# else:
#     # If we are inside this block, it means num1 did NOT beat num2.
#     # Therefore, num2 is the current champion. We only need to test num2 against num3.
#     if num2 > num3:
#         print(f"The second number: {num2} is the greatest of the three.")
#     else:
#         print(f"The third number: {num3} is the greatest of the three.")

# Print the sum of numbers from 1 to 100 using a loop
# sum = 0
# for i in range(1, 101, 1):
#     sum += i

# print(f"The sum of numbers from 1 to 100: {sum}")

# # Print only even numbers from 1 to 20 using continue
# for i in range(1,21,1):
#     if i % 2 != 0:
#         continue
#     print(i)

# WAP to display the factors of n using while loop
n = int(input("Enter the number whose factor to be determined: "))
i = 1
while i <= n:
    if n % i == 0:
        print(f"The factor of {n} is {i}")
    i+= 1
# WAP to display the table of n upto 10 times
n = int(input("Enter the number whose table to display: "))
for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")