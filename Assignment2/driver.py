# CHRISTOPHER HUNT
# driver.py

import random
from network import Network
from MNIST_crit_funcs import fileInput
import numpy as np

size = (784,15,15,10)
net = Network(size)

net.selectionMenu()

## test_file = "/home/chunt/VScode/Data/MNIST/mnist_test.csv"
# test_image, test_label = fileInput(test_file,10000)

# train_file = "/home/chunt/VScode/Data/MNIST/mnist_train.csv"
# train_image, train_label = fileInput(train_file,60000)

# print(net.feedForwardRelu(test_image).T[0])