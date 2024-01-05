import openpyxl
import pandas as pd
import csv
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
csv_filename = (r'C:\Users\jayce\Desktop\6.csv' )
csv_data = []
v45 = []
v457 = []
v479 = []
v49 = []
f = open(csv_filename , 'r')
csv_data = [row for row in csv.reader(f)]
workbook = openpyxl.workbook.Workbook()
worksheet = workbook.active
for row in csv_data:
    worksheet.append(row)

sheet = workbook.worksheets[0]


#<5 5~7 7~9 >9
for i in range(6 , sheet.max_row+1):
    value = float(sheet.cell(row = i , column = 2).value)
    if value < 5 :
        v45.append(value)
    elif value >= 5 and value < 7 :
        v457.append(value)
    elif value >= 7 and value < 9 :
        v479.append(value)
    elif value >= 9 :
        v49.append(value)


x = [1,2,3,4]        
label = ['<5','5~7','7~9','>9']     
h = [len(v45),len(v457),len(v479),len(v49)]   

plt.title('v4download',fontsize=24)
y_major_locator=MultipleLocator(5)
ax=plt.gca()
ax.yaxis.set_major_locator(y_major_locator)


plt.bar(x,h,tick_label=label,width=0.5)  
plt.show()