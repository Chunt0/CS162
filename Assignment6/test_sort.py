# Christopher Hunt
# CS 162
# test_sort.py


import numpy as np
from sort import selection_sort, bubble_sort, insertion_sort, merge_sort

"""
Each one of these tests if the randomly generated list was actually sorted
from smallest to largest by looping through the sorted list and comparing each 
value to the one preceding it, if any value after the indexed value being checked
is smaller than the assertion fails and should generate an error.
"""

def test_selection_sort():
    rand_list = np.random.randint(0,10,10)
    rand_list = selection_sort(rand_list)
    for index in range(0, len(rand_list)-1):
        assert rand_list[index] <= rand_list[index+1]

def test_bubble_sort():
    rand_list = np.random.randint(0,10,10)
    rand_list = bubble_sort(rand_list)
    for index in range(0, len(rand_list)-1):
        assert rand_list[index] <= rand_list[index+1]

def test_insertion_sort():
    rand_list = np.random.randint(0,10,10)
    rand_list = insertion_sort(rand_list)
    for index in range(0, len(rand_list)-1):
        assert rand_list[index] <= rand_list[index+1]

def test_merge_sort():
    rand_list = np.random.randint(0,10,10)
    rand_list = merge_sort(rand_list)
    for index in range(0, len(rand_list)-1):
        assert rand_list[index] <= rand_list[index+1]
