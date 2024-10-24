

def flatten_ragged_list(ragged_list:list)->list:
    temp = []
    for list in ragged_list:
        for i in list:
            temp.append(i)
        
    return temp

print(flatten_ragged_list([[1, 2, 3], [4, 5], [6, 7, 8, 9], [10], [11, 12, 13]]))