import openpyxl
import pandas as pd
import csv
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
class c_sp_pltbar:
    def __init__(self , csv_filename) -> None:
        self.csv_filename = csv_filename
        self.round_ = {'v4_Download':2 , 'v4_Upload':4 , 'v6_Download':3 , 'v6_Upload':5}

    def f_get_all_value(self):
        csv_data = []
        f = open(self.csv_filename , 'r')
        for i in csv.reader(f) : 
            csv_data.append(i)
        workbook = openpyxl.workbook.Workbook()
        worksheet = workbook.active
        for row in csv_data:
            worksheet.append(row)
        self.sheet = workbook.worksheets[0]
        del csv_data , f , workbook ,row

    def f_plt6m_bar(self):
        for k in self.round_:
            range5_ = 0
            range5_7 = 0
            range7_9 = 0
            range_9 = 0
            #<5 5~7 7~9 >9
            for i in range(6 , self.sheet.max_row+1):
                value = float(self.sheet.cell(row = i , column = self.round_[k]).value)
                if value < 5 :
                    range5_ += 1
                elif value >= 5 and value < 7 :
                    range5_7 += 1
                elif value >= 7 and value < 9 :
                    range7_9 += 1
                elif value >= 9 :
                    range_9 += 1
            x = [1,2,3,4]        
            label = ['<5','5~7','7~9','>9']     
            h = [range5_,range5_7,range7_9,range_9]   
            plt.title(k,fontsize=24)
            y_major_locator=MultipleLocator(5)
            ax=plt.gca()
            ax.yaxis.set_major_locator(y_major_locator)
            plt.bar(x,h,tick_label=label,width=0.5)  
            plt.show()


def main ():

    csv_filename = (r'C:\Users\jayce\Desktop\6.csv')
    sp_pltbar = c_sp_pltbar(csv_filename)
    sp_pltbar.f_get_all_value()
    sp_pltbar.f_plt6m_bar()


if __name__ == "__main__" :
    main()