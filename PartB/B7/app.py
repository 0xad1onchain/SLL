import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv('titanic.csv')
df1 = df1.drop(['Ticket'], 1)
df1['Cabin'] = df1['Cabin'].fillna('NOPE')
print('Number of Entries, Attributes:', df1.shape) 
print(df1.keys()) #Print Attributes
print(df1.dtypes) #Print Datatypes
print('Max Age', df1['Age'].max())
print('Min Age', df1['Age'].min())
print('Mean Age', df1['Age'].mean())
ax = df1.plot()
ax.set_xlabel('Age')
ax.set_ylabel('Number of People')
plt.show(block=True)