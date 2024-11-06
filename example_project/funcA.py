from example_project.__wrapper__ import Runtime


def funcA(*args, **kwargs):
    """
     FUNCA Summary of this function goes here  
          Detailed explanation goes here  
      
    """
    return Runtime.call("funcA", *args, **kwargs)
