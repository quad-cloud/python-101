def compare_lists(list_1, list_2):
    list_3 = []
    for element in list_1:
        if (element in list_2) and (element not in list_3):
            list_3.append(element)
    return list_3

def is_even(num):
    return num % 2 == 0

def less_than(input_list, threshold):
    output_list = []
    for element in input_list:
        if element < threshold:
            output_list.append(element)
    return output_list

def first_last(input_list):
    output_list = []
    output_list.append(input_list[0])
    output_list.append(input_list[-1])
    return output_list

def max_3(num_1, num_2, num_3):
    if num_1 >= num_2:
        if num_1 >= num_3:
            return num_1
        else:
            return num_3
    elif num_2 >= num_3:
        return num_2
    else:
        return num_3

def max_of_3(num_1, num_2, num_3):
    if num_1 >= num_2 and num_1 >= num_3:
        return num_1
    if num_2 >= num_2 and num_2 >= num_3:
        return num_2
    if num_3 >= num_1 and num_3 >= num_2:
        return num_3

if(__name__ == '__main__'):
    print(compare_lists([1, 2, 3, 4, 5, 3], [3, 4, 5, 6, 7]))
    print(is_even(5))
    print(is_even(50))
    print(less_than([1, 2, 3, 6, 8, 9, 12, 13], 5))
    print(first_last([1, 2, 3, 6, 8, 9, 12, 13]))
