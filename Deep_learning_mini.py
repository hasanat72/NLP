import numpy
import matplotlib
import sklearn
import pandas

myarray = numpy.array([[1,2,3],[4,5,6]])

rawnames = ['a','b']
colnames = ['one','two','three']

mydataframe= pandas.DataFrame(myarray, index= rawnames, columns=colnames)
print(mydataframe)
