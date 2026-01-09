import pytest
from my_package import my_module
import numpy as np

def test_my_class():    
    arg1 = 1
    arg2 = 2
    my_obj = my_module.My_Class(arg1, arg2)
    result = my_obj.calculate_sum()
    my_obj.display()
    
    assert result == np.float16(3)
    

def test_my_function():
    input_variable = "Test of 'Hello world!'"
    result = my_module.my_function(input_variable)

    assert result == "Test of 'Hello world!'"

if __name__ == "__main__":
    pytest.main()