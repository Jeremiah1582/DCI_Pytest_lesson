import pytest 
import main

# ----------------------test cases ------------------
def test_multiplication():
    assert main.multiply(10,4) == 40 
    assert main.multiply(10000, 25) == 250000 #EDGE CASES testing!!
    assert main.multiply(-10000, -25) == 250000 #EDGE CASES testing!!
    assert main.multiply(-10000, 25) == (-10000)*25 #EDGE CASES testing!!
    
    # TERMS:
    # edge case testing- this is when you test the extremes (unlikely use cases) of your function.
    

    
    
    

    