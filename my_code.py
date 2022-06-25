list_one = ["John", "Mike", "Nick", "Devon", "Lion", "Peter", "Terill", "Arine", "Michael"]
list_two = ["Brandon", "Taras", "Mike", "Alice", "Lion", "Oksana", "John"]

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
print(list_one)
print(list_two)