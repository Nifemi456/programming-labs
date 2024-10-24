from flatten_ragged_list import flatten_ragged_list

def calculate_statistics(ragged_list):
    flat_list = flatten_ragged_list(ragged_list)
    no_of_elements = len(flat_list)
    temp = 0
    for i in flat_list:
        temp += i
    sum_of_elements = temp
    avg_value=temp/no_of_elements
    max_value = flat_list[0]
    for i in flat_list:
        if i > max_value:
            max_value = i
    return (no_of_elements, avg_value, max_value, sum_of_elements)

print(calculate_statistics([[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]))
    