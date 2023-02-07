from dataclasses import dataclass # reduces boiler line code
from openpyxl import Workbook
wb=Workbook()
sheet = wb.active
@dataclass
class People():
    name:str
    no  :int
    age : int

p=[People('pavan',1,23),People('kumar',2,23),People('karnam',3,30)]
data = [[x.name,x.no,x.age]for x in p]
data = [['Name','Num','Age']]+data
for d in data:
    sheet.append(d)
wb.save("../dataset/dtclassdemo.xlsx")
