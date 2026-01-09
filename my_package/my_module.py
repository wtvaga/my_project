#!/usr/bin/env python 

# import of necessary modules for My_Class
import numpy as np

# (in case) import of necessary modules for my_function 

class My_Class:
    def __init__(self, arg1, arg2):
        self.arg1 = np.float16(arg1)
        self.arg2 = np.float16(arg2)
        self.result = np.nan

    def display(self):
        print(f"arg1: {self.arg1}")
        print(f"arg2: {self.arg2}")
        print(f"arg1 + arg2 = {self.result}")

    def calculate_sum(self):
        self.result = self.arg1 + self.arg2
        return self.result


def my_function(input_variable):
    print(input_variable)    
    return input_variable


if __name__ == "__main__":
    
    # istantiation of My_Class and calls of its methods
    arg1 = 1
    arg2 = 2
    my_obj = My_Class(arg1, arg2)
    my_obj.calculate_sum()
    my_obj.display()
        
    
    # import of necessary modules for my_function        
    # call of my_function
    input_variable = "Hello world!"
    my_function(input_variable)