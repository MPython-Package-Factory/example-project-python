from example_project.__wrapper__ import Runtime, MatlabClassWrapper


class classA(MatlabClassWrapper):
    def __init__(self, *args, _objdict=None, **kwargs):
        """
        classA is a class.  
              obj = classA(foo, bar)  
            
              Documentation for classA  
                 doc classA  
            
          
        """
        if _objdict is None:
            _objdict = Runtime.call("classA", *args, **kwargs)
            
        super().__init__(_objdict)

    def _private_method(self, *args, **kwargs):
        """

        """
        return Runtime.call("private_method", *args, **kwargs)
