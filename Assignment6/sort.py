# Christopher Hunt
# CS162
# selection_sort.py

import numpy as np

################################################################################

def selection_sort(sort_list):

    """Selection Sort Function."""

    # Loop through each variable, make it the smallest value.
    for index1 in range(0, len(sort_list)):
        minimum = index1
        # Compare this value to all other values after it in the list, 
        # if smaller, make that index the minimum
        for index2 in range(index1+1, len(sort_list)):
            if sort_list[index2] < sort_list[minimum]:
                minimum = index2
        # This is where all the magic happens -> swap index1 position with the 
        # smallest value left in the list
        sort_list[index1], sort_list[minimum] = sort_list[minimum], sort_list[index1]
    return sort_list

################################################################################

def bubble_sort(sort_list):

    """Bubble Sort Function"""
    # Swap is used as the main loop driver.
    swap = True
    while swap:
        # Reset the main driver condition
        swap = False

        # Loop through the list, larger values are "bubbled" up to the end of the list
        for index in range(0,len(sort_list)-1):
            if sort_list[index] > sort_list[index+1]:
                sort_list[index], sort_list[index+1] = sort_list[index+1], sort_list[index]
                swap = True

    return sort_list

################################################################################

def insertion_sort(sort_list):

    """Insertion Sort Function"""
    for index1 in range(1, len(sort_list)):
        value = sort_list[index1]
        index2 = index1-1

        # Move value towards the beginning of the list as long as it is smaller
        while index2 >= 0 and value < sort_list[index2]:
            sort_list[index2 + 1] = sort_list[index2]
            index2 -= 1

        sort_list[index2 + 1] = value

    return sort_list

################################################################################

def merge(left, right):
    """Helper function for merge_sort"""

    # If left or right is null, return any none NULL list
    if not left or not right:
        return left or right

    # Make the merged list that will be appended to
    merged_list = []

    # Create indexing variables and enter while loop to find smaller values and append merge_list
    i, j = 0, 0
    while len(merged_list) < len(left) + len(right):
        if left[i] < right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1

        if i == len(left):
            merged_list.extend(right[j:])
            break
        if j == len(right):
            merged_list.extend(left[i:])
            break

    return merged_list

def merge_sort(sort_list):

    """Merge Sort Function"""
    # Essential for recursive function, once list is broken down to single values,
    # this function will then move back through the recursive functions merging lists.
    if len(sort_list) < 2:
        return sort_list

    # Split up the initial list using recursive function calls
    middle = len(sort_list) // 2
    left = merge_sort(sort_list[:middle])
    right = merge_sort(sort_list[middle:])

    # Once the list has been sorted and merged using this helper function, return the merged list
    return merge(left,right)

################################################################################

def partition(sort_list, low, high):

    """Quick Sort helper function"""
    pivot = sort_list[high]

    index1 = low - 1

    for index2 in range(low, high):
        if sort_list[index2] <= pivot:
            index1 += 1
            sort_list[index1], sort_list[index2] = sort_list[index2], sort_list[index1]

    sort_list[index1+1], sort_list[high] = sort_list[high], sort_list[index1+1]

    return index1+1

def quick_sort(sort_list, low, high):

    """Quick Sort Function"""
    #
    if low < high:
        partition_index = partition(sort_list, low, high)

        quick_sort(sort_list, low, partition_index-1)
        quick_sort(sort_list, partition_index+1, high)

################################################################################

def heap_sort(sort_list):
    
    """Heap Sort Function"""
    #

    pass

################################################################################
# If you don't have numpy, you can make this list into any list of numbers you would like.
rand_list = np.random.randint(0,10,10)

print(f"Original Random List: \n{rand_list}")

quick_sort(rand_list, 0, len(rand_list)-1)

print(f"Sorted Random List: \n{rand_list}")

