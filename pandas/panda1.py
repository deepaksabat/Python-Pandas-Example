import numpy as np
import pandas as pd 
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data, index=labels)
print(df.loc[:,['animal','age']])
print(df.loc[df.index[[3,4,8]],['animal','age']])
print(df[df['visits']>3])
print(df[df['age'].isnull()])
print(df[(df['animal'] == 'cat')& (df['age']==3)])
print(df[df['age'].between(2,4)])
df.loc['f','age']=1.5
print(df['visits'].sum())
print(df.groupby('animal')['age'].mean())