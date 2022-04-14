#IPython basics # CC means Coursera Code from Coursera class 
#nnw

import numpy as np
from numpy.random import randn 


data = {i : np.random.randn() for i in range(7)}

data2 = {i : randn() for i in range(8)}

print(data)
print(data2)




