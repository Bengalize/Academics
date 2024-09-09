### 1.1 Sigmoid Function
- **basic_sigmoid(x)**: Computes the sigmoid function using the math library, returning \( \frac{1}{1 + e^{-x}} \) for a given real number `x`.
  
- **sigmoid(x)**: Implements the sigmoid function using NumPy, allowing for element-wise computation on arrays.

### 1.2 Sigmoid Gradient
- **sigmoid_derivative(x)**: Computes the derivative of the sigmoid function. It first calculates the sigmoid of `x`, then returns the gradient \( s(1-s) \), where \( s \) is the sigmoid of `x`.

### 1.3 Reshaping Arrays
- **image2vector(image)**: Reshapes a 3D NumPy array (representing an image) into a 1D column vector with shape `(length * height * depth, 1)`.

### 1.4 Normalizing Rows
- **normalize_rows(x)**: Normalizes each row of a NumPy matrix `x` to have unit length (L2 norm).

### 1.5 Softmax
- **softmax(x)**: Computes the softmax function, which normalizes each row of the matrix `x` so that the elements lie between 0 and 1 and sum to 1.

### 2.1 Loss Functions
- **L1(yhat, y)**: Computes the L1 loss, which is the sum of the absolute differences between the predicted labels `yhat` and the true labels `y`.

- **L2(yhat, y)**: Computes the L2 loss (also known as squared error), which is the sum of the squared differences between the predicted labels `yhat` and the true labels `y`.
