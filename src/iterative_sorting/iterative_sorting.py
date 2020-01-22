# If `elements` is a collection, remember it will be passed
# by reference, not value
######################################
# How many loops will be needed to complete this algorithm?
# How do we know when we are ready to swap values?
# And how do we keep track of which values should be swapped?
# What, if anything needs to be returned?


# TO-DO:
# Complete the selection_sort() function below
def selection_sort(arr):
    # print('arr: ', arr)
    arr_len = len(arr)
    # loop through n-1 elements
    for cur_index in range(0, arr_len - 1):

        smallest_index = cur_index

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for remaining_element in range(cur_index + 1, arr_len):
            if (arr[smallest_index] > arr[remaining_element]):
                smallest_index = remaining_element
                # print('smallest_index after assignment ', smallest_index)

        # print(' arr[smallest_index]: ',  arr[smallest_index])
        # print('arr[cur_index]: ', arr[cur_index])
        # TO-DO: swap
        # arr[smallest_index] = arr[cur_index]
        # arr[cur_index] = arr[smallest_index]      # Why doesn't this work?
        # Timing?
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    # print('Ok')
    # print('arr: ', arr)
    return arr


######################################
# 2 1 4 3
# > element[0] = 2
# > range 0 to 4
# >> element[0] = 2
# >> range 0 to 4 - 0 - 1
# >> range 0 to 3
# >> 2 > 1
# >> swap them
# 1 2 4 3
# >> element[1] = 2
# >> 2 > 4
######################################
# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    arr_len = len(arr)
    for element in range(0, arr_len):
        # print('element: ', element)
        for inner_element in range(0, arr_len - element - 1):
            if arr[inner_element] > arr[inner_element + 1]:
                arr[inner_element], arr[inner_element + 1] = arr[inner_element + 1], arr[inner_element]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    return arr
