from example_project.__wrapper__ import Runtime, MatlabClassWrapper


class classA(MatlabClassWrapper):
    def __init__(self, *args, _objdict=None, **kwargs):
        """
        classA is a class.  
              obj = classA(foo, bar)  
            
              Documentation for classA  
                 doc classA  
            
          

        [Matlab code]( https://www.github.com/MPython-Package-Factory/example-project-matlab/buildexample-project-matlab@classAclassA.m )
        """

        if _objdict is None:
            _objdict = Runtime.call("classA", *args, **kwargs)
            
        super().__init__(_objdict)

    def _private_method(self, *args, **kwargs):
        """


        [Matlab code]( https://www.github.com/MPython-Package-Factory/example-project-matlab/buildexample-project-matlab@classAprivateprivate_method.m )
        """

        return Runtime.call("private_method", *args, **kwargs)
