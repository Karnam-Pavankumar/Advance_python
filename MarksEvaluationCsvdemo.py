import pandas as pd
import numpy as np
class Readcsv():
    def Create_df( self,path ):
        self.path = path
        self.df = pd.DataFrame(self.path)
        return self.df
    def total_df( self):

        self.df['total'] = self.df.iloc[:,2:].sum(axis=1)
        return self.df

    def Result( self ):
        self.df['Result'] = np.where((self.df['m1']>=35) & (self.df['m2']>=35) & (self.df['m3']>=35) &
                                     (self.df['m4']>=35) & (self.df['m5']>=35),"pass","fail")
        return self.df
    def avg_df( self):

       self.df['avg']=np.where((self.df['Result'])=='pass',round(self.df['total']/5),0.0)
       return self.df

    def Rank( self):
      self.df['Rank']=np.where((self.df['Result']=='pass'),self.df['avg'].rank(ascending=False),'nA')

      return self.df
obj = Readcsv()
df=pd.read_csv('..//dataset//markcalculation.csv')
print(obj.Create_df(df))
print(obj.total_df())
print(obj.Result())
print(obj.avg_df())
print(obj.Rank())


