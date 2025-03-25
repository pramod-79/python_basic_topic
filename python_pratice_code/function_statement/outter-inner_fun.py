"""
    The outer function takes two arguments, calls a nested function to calculate the sum of squares of
    the arguments, and returns the result.
    
    :param x: 3
    :param y: In the given code snippet, the parameter `y` is the second argument passed to the
    `outer_function` when it is called. In this case, `y` is assigned the value of `4` when
    `outer_function(3, 4)` is called
    :return: The result being returned is 25.
"""
def outer_function(x, y): # 3,4  STEP -1
   
    # Define the nested function
    def inner_function(a, b): # 3,4 STEP- 3
        return a ** 2 + b ** 2
    # Call the nested function and return its result
    result = inner_function(x, y) # STEP- 2 (3,4) x and y as a pass by argument within inner function 
    return result

# Example usage
output = outer_function(3, 4)
print("The result is:", output)
