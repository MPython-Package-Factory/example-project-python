from example_project.__wrapper__ import Runtime


def nested_nested_function(*args, **kwargs):
    """
     NESTED_NESTED_FUNCTION Summary of this function goes here  
          Detailed explanation goes here  
      

    [Matlab code]( https://www.github.com/MPython-Package-Factory/example-project-matlab/nestedA/nestedB/nested_nested_function.m )
    """

    return Runtime.call("nested_nested_function", *args, **kwargs)
