# @Time     :2020/12/11 0011 6:06
# @Author   :Mu Sen
# @Filename :demo_excel文件读写.py


# 本案例具体地址：https://jingyan.baidu.com/article/a681b0de5584c93b184346ba.html
# 此网址介绍很详细

# *****************读取excel***************开始
import xlrd


file_name = r"C:\Users\musen\Desktop\Tong.xls"

workbook = xlrd.open_workbook(file_name)  # 打开工作簿，建立一个工作簿对象

print(workbook.sheet_names())

sheet1 = workbook.sheet_by_index(0)  # 建立一个工作表对象，与下面这两行代码是一样的意思
sheet2 = workbook.sheet_by_name('Sheet1')
sheet3 = workbook.sheets()[0]
print(sheet1)
print(sheet2)
print(sheet3)

print(sheet1.nrows)  # 获取行数
print(sheet1.ncols)  # 获取列数

print(sheet2.nrows)  # 获取行数
print(sheet2.ncols)  # 获取列数

# 获取整行、整列数据
print(sheet1.row_values(0))
print(sheet1.col_values(0))

# 获取一个单元格数据
cell_A = sheet1.cell(1, 1).value
print(cell_A)
print(sheet1.cell(0, 0))
print(sheet1.cell(0, 0).value)
# *****************读取excel***************结束


# *****************写入excel***************开始
import xlwt


stus = [['年', '月'], ['2018', '10'], ['2017', '9'], ['2016', '8']]
excel = xlwt.Workbook()  # 新建excel文件
sheet = excel.add_sheet('测试')  # 新建页签
row = 0
for stu in stus:
    col = 0
    for s in stu:
        sheet.write(row, col, s)  # 开始写入
        col = col + 1
    row = row + 1
excel.save('测试.xls')  # 保存
# *****************写入excel***************结束








