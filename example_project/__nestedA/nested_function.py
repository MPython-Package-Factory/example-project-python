from example_project.__wrapper__ import Runtime


def nested_function(*args, **kwargs):
    """
     NESTED_FUNCTION Summary of this function goes here  
          Detailed explanation goes here  
      

    [Matlab code]( https://www.github.com/MPython-Package-Factory/example-project-matlab/nestedA/nested_function.m )
    """

    return Runtime.call("nested_function", *args, **kwargs)
