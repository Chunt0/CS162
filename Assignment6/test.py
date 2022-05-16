# Christopher Hunt
# CS162
# pytest.py

import numpy as np
from sort import selection_sort, bubble_sort, insertion_sort, merge_sort 


def main():
# If you don't have numpy, you can make this list into any list of numbers you would like.
    test_on = True

    while test_on:
        try:
            rand_list = np.random.randint(0,10,10)
            selection = int(input("1. Selection Sort\n2. Bubble Sort\n3. Insertion Sort\n4. Merge Sort\n5. Exit\n:: "))
            if selection == 1:
                print(f"\nOriginal Random List:\n{rand_list}")
                rand_list = selection_sort(rand_list)
                print(f"\nSelection Sorted List:\n{rand_list}\n")
            elif selection == 2:
                print(f"\nOriginal Random List:\n{rand_list}")
                rand_list = bubble_sort(rand_list)
                print(f"\nBubble Sorted List:\n{rand_list}\n")
            elif selection == 3:
                print(f"\nOriginal Random List:\n{rand_list}")
                rand_list = insertion_sort(rand_list)
                print(f"\nBubble Sorted List:\n{rand_list}\n")
            elif selection == 4: 
                print(f"\nOriginal Random List:\n{rand_list}")
                rand_list = merge_sort(rand_list)
                print(f"\nMerge Sorted List:\n{rand_list}\n")
            elif selection == 5:
                print("\nGood Bye!")
                test_on = False
            else:
                print("\nYou must enter an integer between 1 and 5.\n")

        except:
            print("\nIncorrect input. Please press an integer between 1 and 5.\n")

if __name__ == "__main__":
    main()
