#要求：1）合并10个工作簿，表名不具有规律性 （北京.xlsx,上海.xlsx...郑州.xlsx)
import os
import xlrd
import pandas as pd

#获取所有需要合并的工作簿路径，生成list
def file_name(file_dir): 
    list=[]
    for file in os.listdir(file_dir):
        if os.path.splitext(file)[1] == '.xlsx':
            list.append(file)
    return list

path = r'‎⁨/Users/apple/Desktop/FYP/py/'
wks = file_name(path)

data = []   #定义一个空list
for i in range(len(wks)):
    read_xlsx = xlrd.open_workbook(path + '\\' + wks[i])
    sheet1 = read_xlsx.sheets()[0] #查看sheet1的数据
    nrow =  sheet1.nrows
    title = sheet1.row_values(0)   #查看第1行数据
    for j in range(1,nrow): #逐行打印
        data.append(sheet1.row_values(j))

content= pd.DataFrame(data)
#修改标题
content.columns= title
#写入文件
#写入csv文件
#content.to_csv(path+'\\py_union.xlsx', sep=',', header=True, index=False)
#写入excel文件
content.to_excel(path+'\\py_union2.xlsx', header=True, index=False)