# CHRISTOPHER HUNT
# driver.py

import random
from network import Network
from MNIST_crit_funcs import fileInput
import numpy as np

def main():
    size = (784,15,15,10)
    net = Network(size)

    net.selectionMenu()

if __name__ == "__main__":
    main()