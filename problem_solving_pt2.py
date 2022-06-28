import math
# 1. Happy Numbers a. https://en.wikipedia.org/wiki/Happy_number
#       b. A happy number is a number defined by the following process: starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1. An example of a happy number is 19
#       c. Write a method that determines if a number is happy or sad         

# def happy_number():
#     squared_input_number = int(input("Enter a number: "))**2 # Square of input number
#     string_numbers = str(squared_input_number)
#     list_of_string_numbers = []
#     is_happy_number = False
#     while is_happy_number == False:    
#         for str_number in string_numbers:
#             list_of_string_numbers.append(str_number)
#         list_length = len(list_of_string_numbers)
#         index = 0
#         sum_of_squared_numbers = int(list_of_string_numbers[index])**2 + int(list_of_string_numbers[index + 1])**2
#         if sum_of_squared_numbers == 1:
#             is_happy_number = True
#         else:
#             list_of_string_numbers.clear()
#             string_numbers = str(sum_of_squared_numbers)
#     print("Number is happy!")

def happy_number():
    input_number = input("Enter a number: ")
    sum_of_numbers = 0
    
    for number in input_number:  #has to be string to iterate
        number = int(number)**2
        sum_of_numbers += number
    if sum_of_numbers == 1:
        print(f"{input_number} is happy number!")
    i = 0
    while sum_of_numbers != 1:
        string_number = str(sum_of_numbers)
        sum_of_numbers = 0
        for number in string_number:
            number = int(number)
            sum_of_numbers += number**2
        if sum_of_numbers == 1:
            print(f"{input_number} is a happy number!")
        elif sum_of_numbers != 1 or i < 10:
            i += 1
        else:
            print(f"{input_number} is sad")
            break

happy_number()

# 2. Prime Numbers
#       a. A prime number is a number that is only divisible by one and itself.
#       b. Write a method that prints out all prime numbers between 1 and 100

# 3. Fibonacci
#       a. A series of numbers in which each number (Fibonacci number) is the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.
#       b. Write a method that does the Fibonacci sequence starting at 1
#       c. HARDER VERSION: Write a method that does the Fibonacci sequence starting at a number that a user inputs