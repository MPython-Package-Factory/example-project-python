from example_project.__wrapper__ import Runtime


def nested_function(*args, **kwargs):
    """
     NESTED_FUNCTION Summary of this function goes here  
          Detailed explanation goes here  
      
    """
    return Runtime.call("nested_function", *args, **kwargs)