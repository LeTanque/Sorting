import math


####################################################################
# TK Challenge #####################################################
####################################################################
# Write a recursive search function that receives as input an
# array of integers and a target integer value. This function
# should return True if the target element exists in the array,
# and False otherwise.
####################################################################
# What would be the base case(s) we’d have to consider for
# implementing this function?
# True or False. Ending on True
####################################################################
# How should our recursive solution converge on our base case(s)?
# range of 0 to end of list
####################################################################
def recursive_search(int_arr, target):
    for i in range(0, len(int_arr)):
        # print('int_arr[i] : ', int_arr[i])
        if int_arr[i] == target:
            # print("Yay this is working!")
            print('True: ', True)
            return True
        if len(int_arr) == 1 and int_arr[i] != target:
            print('False: ', False)
            return False
        # print('len(int_arr): ', len(int_arr))
        return i * recursive_search(int_arr[i + 1:len(int_arr)], target)


print('recursive_search: ', recursive_search([1, 2, 4, 56, 7], 4))


# QUESTION: Why is it that I cannot return "False". If I print it, it works.
# but otherwise, I don't get a direct boolean response.
# integer_array = [0, 2, 4, 3, 6, 10, 22, 1]
# target = 3
# print('recursive_search: ', recursive_search(integer_array, target))
####################################################################
# Recursion example. Simple.
def recurse_factorial(n):
    print('n: ', n)
    if n == 0:
        return 1
    return n * recurse_factorial(n - 1)


# print('recurse_factorial(10): ', recurse_factorial(10))
# print("math", math.log(10000, 10), 2 ** 4)
####################################################################
####################################################################
####################################################################


# Method 1
# (O(n1 * n2) Time and O(1) Extra Space)
# Create an array arr3[] of size n1 + n2.
# Copy all n1 elements of arr1[] to arr3[]
# Traverse arr2[] and one by one insert elements
# (like insertion sort) of arr3[] to arr1[].

# TO-DO: complete the helper function below to merge 2 sorted arrays
# NO SORT
# def merge(arrA, arrB):
#     len_arrA = len(arrA)
#     len_arrB = len(arrB)
#     sorted_arr = []
#     for i in range(0, len_arrA):
#         sorted_arr.append(arrA[i])
#     for j in range(0, len_arrB):
#         sorted_arr.append(arrB[j])
#     sorted_arr.sort()
#     return sorted_arr


# Solution inspired by Brady
def merge(arr_a, arr_b):
    total_elem = len(arr_a) + len(arr_b)
    merged_arr = [None] * total_elem
    # Declare indices for each sublists
    a = 0
    b = 0
    for i in range(total_elem):
        # Check if either list is empty
        if a >= len(arr_a):
            merged_arr[i] = arr_b[b]
            b += 1
        elif b >= len(arr_b):
            merged_arr[i] = arr_a[a]
            a += 1
        # Otherwise compare and append the smallest
        elif arr_a[a] < arr_b[b]:
            merged_arr[i] = arr_a[a]
            a += 1
        else:
            merged_arr[i] = arr_b[b]
            b += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
# Step 1: Split out list into sub lists until
# they are all len 1 or less
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    # Divide in half
    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2:]
    # Sort the left
    left = merge_sort(left)
    # Sort the right
    right = merge_sort(right)
    # Then merge together
    return merge(left, right)


# # STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr

# def merge_sort_in_place(arr, l, r):
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# hint: check out
# https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

#     return arr
