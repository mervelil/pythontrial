import numpy as np
import glob



py_list=[1,2,3,4,6,7,8]
result=np.arrange(10,100,1)
result =np.zeros(10)
result =np.linspace(0,100,5)
result =np.random.randint(0,100)
nparray=np.arange(50)

rmulti =nparray.reshape(5,10)
print(rmulti.sum(axis=1))
#numpy array
np_array =np.array([1,2,3,5,6])
print(type(py_list))
print(type(np_array))