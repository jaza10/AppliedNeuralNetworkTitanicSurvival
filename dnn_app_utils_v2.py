import numpy as np
import matplotlib.pyplot as plt
import h5py

# DOWNLOAD THIS FILE FROM THE COURSERA DEEP LEARNING AND NEURAL NETWORKS
# COURSE WEEK 4 PROGRAMMING ASSIGNMENTS


def sigmoid(Z):

	# Import code here
    return A, cache

def relu(Z):
	# Import code here
    return A, cache


def relu_backward(dA, cache):
	
	# Import code here
    
    return dZ

def sigmoid_backward(dA, cache):

	# Import code here
    
    return dZ



def initialize_parameters(n_x, n_h, n_y):
	
	# Import code here
    
    return parameters     


def initialize_parameters_deep(layer_dims):
	
   	# Import code here
        
    return parameters

def linear_forward(A, W, b):
	
    # Import code here
    
    return Z, cache

def linear_activation_forward(A_prev, W, b, activation):
	
   	# Import code here

    return A, cache

def L_model_forward(X, parameters):
	
    # Import code here
		
    return AL, caches

def compute_cost(AL, Y):
	
	# Import code here
		
    return cost

def linear_backward(dZ, cache):
	
	# Import code here
		
    return dA_prev, dW, db

def linear_activation_backward(dA, cache, activation):
	
	# Import code here
	
    return dA_prev, dW, db

def L_model_backward(AL, Y, caches):
	
	# Import code here
	
    return grads

def update_parameters(parameters, grads, learning_rate):
	
	# Import code here
	
    return parameters

def predict(X, y, parameters):
	
	# Import code here
	
    return p
