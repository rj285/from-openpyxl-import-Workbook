from openpyxl import Workbook

wb = Workbook()

ws = wb.active

data = [
    
    ["Name","Price","Origin"],
    ["Apple",30,"India"],
    ["Banana",25,"China"],
    ["Cherry",35,"Malta"],
    ["Tomoto",25,"Vythiri"]
]

for row_data in data:
    ws.append(row_data)
    
wb.save('wb4.xlsx')