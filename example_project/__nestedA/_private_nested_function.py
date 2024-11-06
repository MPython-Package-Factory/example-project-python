from example_project.__wrapper__ import Runtime


def _private_nested_function(*args, **kwargs):
    """
     PRIVATE_NESTED_FUNCTION Summary of this function goes here  
          Detailed explanation goes here  
      
    """
    return Runtime.call("private_nested_function", *args, **kwargs)
