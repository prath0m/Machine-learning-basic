import numpy
import pandas

arr=numpy.array([
    ['england','usa','germany','japan'],
    ['london','washington','berlin','tokyo'],
    ['pound','dollar','euro','yen']
])

df=pandas.DataFrame(arr)
print(df)