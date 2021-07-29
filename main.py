import pan

n = [1,2,3,4,5]
ind = (1,2,3,4,5)
s1 = pd.Series(n, ind)
s1
print(s1)

b=[12,23,1,34,3,5,22]
n.append(b)
print(n)
b.pop()
print(b)


fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)

import numpy as np
index=[1,2,3,4,5]
arr=np.random.randn(5,5)
col=['A','B','C','D','E']
df1=pd.DataFrame(arr,index=index,columns=col)#creating a data frame
print(df1)


