# Christopher Hunt
# CS162
# pytest.py

import numpy as np
from sort import selection_sort, bubble_sort, insertion_sort, merge_sort 


def main():
# If you don't have numpy, you can make this list into any list of numbers you would like.
    rand_list = np.random.randint(0,10,10)

    print(f"Original Random List: \n{rand_list}")

    rand_list = bubble_sort(rand_list)

    print(f"Sorted Random List: \n{rand_list}")


if __name__ == "__main__":
    main()
