import pandas as pd

d = {'Teams':["india","england"],
     'Rank':[1,2],
     'winpercen':['60%','40%']
}
df = pd.DataFrame(d)
#print(df)
df.rename(columns={"Rank":"Ranking"},inplace = True)
#print(df)
print(df.iloc[:3,-1])
