
# 1. Create a function that is going to take two parameters, which are lists!
# 2. Two lists should be compared and if there is any matches - remove a match from one list and keep it in the other.
# 3. If there is some left objects that didn't match - add them to the first list and remove from the second list.
# 4. Return unique list to the function!

list_one = ["John", "Mike", "Nick", "Devon", "Lion", "Peter", "Terill", "Arine", "Michael"]
list_two = ["Brandon", "Taras", "Mike", "Alice", "Lion", "Oksana", "John"]

def two_lists_make_in_one(list1, list2):
    length_list_one = len(list_one)
    length_list_two = len(list_two)
    if length_list_one >= length_list_two:
        iterations = length_list_one
    else:
        iterations = length_list_two
    i = iterations
    for name in list_one:
        if i == 0:
            break
        if i <= length_list_one:
            if name in list_two:
                list_two.remove(name)           
            i -= 1
    for name in list_two:
        if name not in list_one:
            list_one.append(name)
    list_two.clear()
    return list_one

print("Testing MacOS GitHub")
print(two_lists_make_in_one(list_one, list_two))