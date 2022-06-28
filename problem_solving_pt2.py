import math
# 1. Happy Numbers a. https://en.wikipedia.org/wiki/Happy_number
#       b. A happy number is a number defined by the following process: starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1. An example of a happy number is 19
#       c. Write a method that determines if a number is happy or sad         

def happy_number():
    input_number = input("Enter a number: ")
    sum_of_numbers = 0
    
    for number in input_number:  #has to be string to iterate
        number = int(number)**2
        sum_of_numbers += number
    if sum_of_numbers == 1:
        print(f"{input_number} is happy number!")
    peak_number = 0
    while sum_of_numbers != 1:
        string_number = str(sum_of_numbers)
        sum_of_numbers = 0
        for number in string_number:
            number = int(number)
            sum_of_numbers += number**2
        if sum_of_numbers == 1:
            print(f"{input_number} is a happy number!")
        elif sum_of_numbers > peak_number:
            peak_number = sum_of_numbers
        elif sum_of_numbers == peak_number:
            print(f"Number {input_number} is sad!")
            break

happy_number()

# 2. Prime Numbers
#       a. A prime number is a number that is only divisible by one and itself.
#       b. Write a method that prints out all prime numbers between 1 and 100

# 3. Fibonacci
#       a. A series of numbers in which each number (Fibonacci number) is the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.
#       b. Write a method that does the Fibonacci sequence starting at 1
#       c. HARDER VERSION: Write a method that does the Fibonacci sequence starting at a number that a user inputs