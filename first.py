# Create a function that takes a list as a parameter,
# and returns a new list with every second element from the orignal list
# It should raise an error if the parameter is not a list
# example: [1, 2, 3, 4, 5] should produce [2, 4]

def second_element(raw_list):
    new_list = []
    for element in raw_list[1::2]:
        new_list += [element]
    return new_list

print(second_element([1, 2, 3, 4, 5]))
