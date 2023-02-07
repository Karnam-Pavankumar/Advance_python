import openpyxl
from openpyxl import Workbook
from pythonpandas import salescaldemo
import pandas as pd
from pandas import read_excel
from openpyxl.chart import LineChart,Reference
import numpy as np

df1 = pd.read_excel("..//dataset//hcl_sales.xlsx",sheet_name = "JAN_Sales")
df2 = pd.read_excel("..//dataset//hcl_sales.xlsx",sheet_name = "FEB_Sales")
df3 =(pd.merge(df1,df2,how='outer'))
path ="..//dataset//hcl_sales.xlsx"
with pd.ExcelWriter(path) as writer:
    writer.book = openpyxl.load_workbook(path)
    df3.to_excel(writer,sheet_name = "merge_sales")

