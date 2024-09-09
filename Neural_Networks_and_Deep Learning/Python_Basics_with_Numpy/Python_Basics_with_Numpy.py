#### 1. Building basic functions with numpy
### 1.1 Sigmoid Function, np.exp()
## Basic Sigmoid : 

# Function that returns the sigmoid of a real number x use math.exp(x)

import math
from public_tests import *

def basic_sigmoid(x):    
    s = 1/(1+math.exp(-x))
    return s
    
print("basic_sigmoid(1) = " + str(basic_sigmoid(1)))

basic_sigmoid_test(basic_sigmoid)

# Implementing the Sigmoid using Numpy

def sigmoid(x):

    s = 1/(1+np.exp(-x))
     
    return s
    
t_x = np.array([1, 2, 3])
print("sigmoid(t_x) = " + str(sigmoid(t_x)))

sigmoid_test(sigmoid)

### 1.2 - Sigmoid Gradient

## Sigmoid Derivative

# sigmoid_grad()

def sigmoid_derivative(x):
    s = sigmoid(x)
    ds = s*(1-s)
    return ds
    
t_x = np.array([1, 2, 3])
print ("sigmoid_derivative(t_x) = " + str(sigmoid_derivative(t_x)))

sigmoid_derivative_test(sigmoid_derivative)

### 1.3 - Reshaping Arrays (np.shape, np.reshape)
## image2vector()

def image2vector(image):
    """
    Argument:
    image -- a numpy array of shape (length, height, depth)
    
    Returns:
    v -- a vector of shape (length*height*depth, 1)
    """

    v =  image.reshape((image.shape[0]*image.shape[1]*image.shape[2],1))
        
    return v
    
t_image = np.array([[[ 0.67826139,  0.29380381],
                     [ 0.90714982,  0.52835647],
                     [ 0.4215251 ,  0.45017551]],

                   [[ 0.92814219,  0.96677647],
                    [ 0.85304703,  0.52351845],
                    [ 0.19981397,  0.27417313]],

                   [[ 0.60659855,  0.00533165],
                    [ 0.10820313,  0.49978937],
                    [ 0.34144279,  0.94630077]]])

print ("image2vector(image) = " + str(image2vector(t_image)))

image2vector_test(image2vector)

### 1.4 Normalizing Rows

## normalize_row()

def normalize_rows(x):
    """    
    Argument:
    x -- A numpy matrix of shape (n, m)
    
    Returns:
    x -- The normalized (by row) numpy matrix. You are allowed to modify x.
    """

    x_norm = np.linalg.norm(x,ord = 2, axis = 1, keepdims = True)
    
    x = x/x_norm
   
    return x
    
x = np.array([[0., 3., 4.],
              [1., 6., 4.]])
print("normalizeRows(x) = " + str(normalize_rows(x)))

normalizeRows_test(normalize_rows)

## softmax()
def softmax(x):
    """
    Argument:
    x -- A numpy matrix of shape (m,n)

    Returns:
    s -- A numpy matrix equal to the softmax of x, of shape (m,n)
    """

    x_exp = np.exp(x)
    
    x_sum = np.sum(x_exp, axis = 1, keepdims = True)
    
    s = x_exp/x_sum
        
    return s
    
t_x = np.array([[9, 2, 5, 0, 0],
                [7, 5, 0, 0 ,0]])
print("softmax(x) = " + str(softmax(t_x)))

softmax_test(softmax)

#### 2. Vectorization
### 2.1 Implementing L1 and L2 loss functions
# L1
def L1(yhat, y):
    """
    Arguments:
    yhat -- vector of size m (predicted labels)
    y -- vector of size m (true labels)
    
    Returns:
    loss -- the value of the L1 loss function defined above
    """
    
    loss = np.sum(abs(yhat-y))
        
    return loss
    
yhat = np.array([.9, 0.2, 0.1, .4, .9])
y = np.array([1, 0, 0, 1, 1])
print("L1 = " + str(L1(yhat, y)))

L1_test(L1)

# L2 
def L2(yhat, y):
    """
    Arguments:
    yhat -- vector of size m (predicted labels)
    y -- vector of size m (true labels)
    
    Returns:
    loss -- the value of the L2 loss function defined above
    """
  
    loss = np.sum(np.dot(y-yhat,y-yhat))
        
    return loss
    
yhat = np.array([.9, 0.2, 0.1, .4, .9])
y = np.array([1, 0, 0, 1, 1])

print("L2 = " + str(L2(yhat, y)))

L2_test(L2)

