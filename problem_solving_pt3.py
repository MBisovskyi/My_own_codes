# 1. Given an array of integers, return indices of the two numbers such that they add up to a specific 
#    target. You may assume that each input would have exactly one solution, and you may not use 
#    the same element twice. 
#       a. Use Case: 
#           i. Given numbers in an array: [5, 17, 77, 50]  
#           ii. Target: 55

# def fifty_five_number():
#     list = [5, 17, 77, 50]
#     number = input("Enter a first number: ")
#     list.append(number)
#     return list[0] + list[3]

# result = fifty_five_number()
# print(result)

# 2. Palindrome is a word, phrase, or sequence that reads the same backward as forward i.e. 
#    madam. Write code that takes a user input and checks to see if it is a Palindrome and reports 
#    the result. You must handle spaces. 

# def is_palindrome():
#     input_word = input("Type in something to check if it is a palindrome!: ")
#     word = input_word.lower()
#     reversed_word = ""
#     for index in range(len(word)-1, -1, -1):
#         reversed_word += word[index]
#     if reversed_word == word:
#         print(f'"{input_word}" is a palindrome!')
#     else:
#         print(f'"{input_word}" is NOT a palindrome!')
        
# is_palindrome()

# 3. Given a list of integers, return a bool that represents whether or not all integers in the list can 
#    form a sequence of incrementing integers 
#       a. Use case:  
#           i. {5, 7, 3, 8, 6} → false (no 4 to complete the sequence) 
#           ii. {17, 15, 20, 19, 21, 16, 18} → true

def is_incrementing_integers(list_of_integers):
    index = 0
    while index != len(list_of_integers) - 1:
        if list_of_integers[index] in list_of_integers and list_of_integers[index] + 1 in list_of_integers or list_of_integers[index] == max(list_of_integers):
            index += 1
            if index == len(list_of_integers) - 1:
                return True
        else: 
            return False
            
list_of_integers = [23, 20, 25, 21, 22, 27, 26, 29]
result = is_incrementing_integers(list_of_integers)
print(result)

# and number[len(list_of_integers) - 1] == max(list_of_integers): 