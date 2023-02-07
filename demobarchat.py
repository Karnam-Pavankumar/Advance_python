from openpyxl import Workbook
from openpyxl.chart import BarChart,Reference
wb=Workbook()
sheet=wb.active
sales_data=[["product","online","store"],
           [1,20,30],
           [2,30,49],
           [3,40,50],
           [4,50,80],
           [5,60,70],
           [6,90,80],
           [7,90,30]
           ]
for row in sales_data:
    sheet.append(row)
chart=BarChart()
data=Reference(worksheet=sheet,min_row=1,max_row=8,min_col=2,max_col=3)
chart.add_data(data,titles_from_data=True)
sheet.add_chart(chart,"E2")
wb.save("..\\dataset\\barchat.xlsx")