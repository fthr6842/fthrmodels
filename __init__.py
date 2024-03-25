#Make sure that you have pip install these modules.
from fthrmodels import LinearRegression as lrs
from fthrmodels import TtestPvalue as tp
from fthrmodels import Plot as plt
from fthrmodels import Tools as Tl
__all__=['lrs', 'tp', 'plt', 'Tl']
if __name__=="__main__": print("The purpose of this file, __init__.py, is \
to import the modules for main.py")
