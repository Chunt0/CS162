# CHRISTOPHER HUNT
# network.py

import numpy as np
from MNIST_crit_funcs import sigmoid, relu, softmax, fileInput


class Network:
    def __init__(self,sizes):
        """Initializes the random weights and biases matrices. Also holds the sizes 
        and number of layers variables. Tricky to build weights and biases"""

        self.sizes = sizes
        self.num_layers = len(self.sizes)
        self.weights = [np.random.randn(x,y) for x,y in zip(self.sizes[1:], self.sizes[:-1])]  # (from index 1 until the end, from index 0 to one before the end)
        self.biases = [np.random.randn(y,1) for y in self.sizes[1:]] # (from index 1 until the end, always 1)

    def feedForwardRelu(self, a):
        """Return the output of the network if "a" is input using ReLU and softmax as 
        activation functions - ReLU on all layers except the final which uses a softmax
        function to return values between 0 - 1 """
        # Both the weight and bias matrices have the same amount of layers (in this instance it is two, in each layer the matrices have the same rows but different collumn amount)
        last = len(self.biases)-1
        count = 0
        for b, w in zip(self.biases, self.weights): 
            if(count != last):
                a = relu((np.dot(w,a) + b)) # Perform the sigmoid activation function to output the "neurons" activation after processing
                count += 1
            else:
                a = softmax(np.dot(w,a)+b)
        return a

    def feedForwardSigmoid(self, a):
        """Returns the output of the network if "a" is the input using the Sigmoid
        function as the activation function on all layers"""
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w,a)+b)
            return a

    def stochasticGradientDescent(self, training_data, epochs, mini_batch_size, eta, test_data=None):
        """Finding Global Minima -> in this case minimizing the cost function. Stochastic Gradient Descent is designed such that
        we can better avoid getting caught in local minima to find the global minima."""
        if test_data: n_test = len(test_data)
        pass

##########################################################################################################

#[*] Here is my selection menu where I utilize try and except clauses and access my file reading function. 
    def selectionMenu(self):
        on = True
        try:
            file = input("Provide path to Test or Train csv file: ")
            image, label = fileInput(file, 10000)
            while(on):
                          
                print("What would you like to do?\n1. Feed Forward with ReLU\n2.Feed Forward with Sigmoid\n3. Exit\n")
                selection = int(input(":: "))
                if(selection == 1):
                    print(self.feedForwardRelu(image))
                elif(selection == 2):
                    print(self.feedForwardSigmoid(image))
                elif(selection == 3):
                    print("\nGood Bye!")
                    on = False
                else:
                    print("\nWhat ever you entered didn't make sense. Try again.\n")

        except ValueError:
            print("\n####VALUEERROR####\nYOU MUST HAVE ENTERED A CHARACTER STRING WHEN YOU SHOULD HAVE ENTERED AN INTEGER...")
        except FileNotFoundError:
            print("\n####FILENOTFOUNDERROR####\nTHE FILE PATH YOU ENTERED MUST HAVE BEEN WRONG...")
        except:
            print("\n####UNKNOWNERROR####\nI DON'T KNOW WHAT YOU DID WRONG...")



