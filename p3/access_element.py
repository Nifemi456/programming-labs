def access_element(ragged_list, i ,j):
    element = None
    error = 0
    if ragged_list==None:
        error = 3
        return (error, element)
    try:
        temp = ragged_list[i]
    except IndexError:
        error = 1
        return (error, element)
    try:
        element = temp[j]
        return (error, element)
    except IndexError:
        error = 2
        return (error, element)
    


ex_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10], [11, 12, 13]]
print(access_element(ex_list,2,5))