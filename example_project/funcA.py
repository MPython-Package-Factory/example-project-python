from example_project.__wrapper__ import Runtime


def funcA(*args, **kwargs):
    """
     FUNCA Summary of this function goes here  
          Detailed explanation goes here  
      

    [Matlab code]( https://www.github.com/MPython-Package-Factory/example-project-matlab/buildexample-project-matlabfuncA.m )
    """

    return Runtime.call("funcA", *args, **kwargs)
