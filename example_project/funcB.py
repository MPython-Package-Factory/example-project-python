from example_project.__wrapper__ import Runtime


def funcB(*args, **kwargs):
    """
     FUNCB Summary of this function goes here  
          Detailed explanation goes here  
      

    [Matlab code]( https://www.github.com/MPython-Package-Factory/example-project-matlab/<rfilepath> )
    """

    return Runtime.call("funcB", *args, **kwargs, nargout=0)
