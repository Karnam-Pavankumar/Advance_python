import pandas as pd
import numpy as np
df = pd.read_csv('..//dataset//tested.csv')
#print(df)
print(df.shape)
#print(df.isnull)
#print(df.isna().any())
#print(df.isna().any().sum())
#print(df.describe)
#print(df.Survived)
df.drop(['Cabin'],axis=1,inplace=True)
#print(df)
df.fillna(method='ffill',inplace=True)
#print(df)
#print(pd.crosstab(index=df['Sex'],columns=df['Survived']))
#print(df.groupby(['Sex','Survived'])['Survived'].count())
#print(df.groupby(['Sex','Embarked'])['Embarked'].count())
#print(pd.crosstab(index=df['Sex'],columns=df['Embarked']))
#print(pd.pivot_table(df,index = ['Sex','Age'],aggfunc = np.sum))
#print(df.sort_values(by = ['Pclass','Fare','Ticket','Embarked'],ascending = False))
df['Survived'] = df["Survived"].apply(lambda val:'yes' if val==1 else 'NO')
print(df)


