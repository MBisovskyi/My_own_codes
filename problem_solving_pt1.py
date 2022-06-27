# Reverse a string (HINT: Review the Algorithms + Problem Solving PowerPoint!)
#       a. Write code that takes a string as input and returns the string reversed
#       b. i.e. “Hello” will be returned as “olleH”

def revers_string_input():
    string = input("Write something: ")
    reversed_string = ""
    for index in range(len(string) -1, -1, -1):
        reversed_string += string[index]
    print(reversed_string)

revers_string_input()

# 2. Capitalize letter
#       a. Write code that takes a string as input and capitalize the first letter of each word. Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World”

def capitalize_first_letter():
    string = input("Write something: ")
    string_split = string.split(" ") # returns a list of words
    list_of_words = []
    for word in string_split:
        capitalized_word = word.capitalize()
        list_of_words.append(capitalized_word)
    for word in list_of_words:
        string = " ".join(list_of_words)
    print(string)
    
capitalize_first_letter()


# 3. Palindrome
#       a. A word, phrase, or sequence that reads the same backward as forward i.e. madam
#       b. Write code that takes a user input and checks to see if it is a Palindrome and reports the result

def is_palindrome():
    string = input("Write something: ")
    reversed_string = ""
    for index in range(len(string) -1, -1, -1):
        reversed_string += string[index]
    if string == reversed_string:
        print(f'"{string}" is a palindrome! Check it out: {string} = {reversed_string}')
    else:
        print(f'"{string}" is not a palindrome.')

is_palindrome()


# 4. BONUS CHALLENGE: Compress a string of characters
#       a. For example, an input of "aaabbbbbccccaacccbbbaaabbbaaa" would compress to "3a5b4c2a3c3b3a3b3a"

def string_compressor():
    string = input("Write something to compress: ")
    length = len(string)
    index = 0
    counter = 1
    commpressed_string = ""
    while index != length:
        counter = 1
        while (index < len(string) - 1) and string[index] == string[index + 1]:
            counter += 1
            index += 1
        if counter == 1:
            commpressed_string += str(string[index])
            index += 1
        else:
            commpressed_string += str(counter) + str(string[index])
            index += 1
    return commpressed_string       

result = string_compressor()
print(result)
