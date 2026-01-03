import pandas as pd
df1 = pd.read_csv('C:/git/Homework/Week3/Data/2501.csv')
df2 = pd.read_csv('C:/git/Homework/Week3/Data/2502.csv')
df3 = pd.read_csv('C:/git/Homework/Week3/Data/2503.csv')
df4 = pd.read_csv('C:/git/Homework/Week3/Data/2504.csv')
df5 = pd.read_csv('C:/git/Homework/Week3/Data/2505.csv')
df6 = pd.read_csv('C:/git/Homework/Week3/Data/2506.csv')
df = pd.concat([df1, df2, df3, df4, df5, df6], ignore_index=True)
print(df.columns)