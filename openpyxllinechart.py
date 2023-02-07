from openpyxl import Workbook
from openpyxl.chart import LineChart,Reference
wb=Workbook()
sheet=wb.active
sales_data=[["States","Recovery","Death"],
           ['Ap',39,3],
           ['Mp',30,49],
           ['ts',40,50],
           ['tn',50,80],
           ['up',60,70],
           ['j&k',90,30],
           ['goa',90,30]
           ]
for row in sales_data:
    sheet.append(row)
chart=LineChart()
data=Reference(worksheet=sheet,min_row=1,max_row=8,min_col=2,max_col=3)
chart.add_data(data,titles_from_data=True)
sheet.add_chart(chart,"E2")
wb.save("..\\dataset\\linechart.xlsx")