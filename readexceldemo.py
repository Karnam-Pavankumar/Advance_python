import pandas as pd
import numpy as np
exldata1 = pd.read_excel("..//dataset/Emp.xlsx")
print(exldata1)
exldata2 = pd.read_excel("..//dataset/department.xlsx")
print(exldata2)
#print(exldata2.compare(exldata1))
#data3 = np.where(exldata1['emp_id' ]==exldata2['dept_id'],True,exldata2['dept_id']-exldata1['emp_id'])
data3 = np.where(exldata1['emp_id' ]==exldata2['dept_id'],"yes","No")
print(data3)