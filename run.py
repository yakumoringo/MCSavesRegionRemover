"""
MC地图存档指定删除器
核心工作原理
1.根据xls文件
2.对xls文件指定行列添加至list
3.令存档里的文件名为一个list
4.两个list取反，并且删除非xls表格指定的文件
5.进行对下一个维度操作


"""
#import环节
import os
import os.path
import xlrd

tempSetFilenames=set()
tempSetCellnames=set()
tempSetDelnames=set()
rootMenu=os.getcwd()


#检查当前目录下是否有名为level.dat的文件
if os.path.isfile('./level.dat'):
    #debug:print('test1')
    #检查当前目录下是否有名为region.xls的文件
    if os.path.isfile('./region.xls'):
        #debug:print('test1')
        #对xls文件进行操作
        opSheet=xlrd.open_workbook('./region.xls').sheet_by_index(0)
        #获得要进行操作的sheet
        for i in range(1,opSheet.ncols):
            #从第二列到最有一个有效列的for语句，i为迭代变量
            if opSheet.cell_value(0,i)=='':
                #判断该列第一行文本，如果为空则进入region文件夹
                #如果不为空，则进入单元格的值所对应的文件夹
                tempPath=os.path.join(rootMenu,'region')
                #进入./region文件夹
            else:
                tempPath=os.path.join(rootMenu,opSheet.cell_value(0,i),'region')
                #进入DIMxxx文件夹
            os.chdir(tempPath)
            #进入相对应的文件夹
            #print(tempPath)
            for m,a in enumerate(opSheet.col_values(i,1)):
                if a!='':
                    tempSetCellnames.add(a)

            for m,a in enumerate(os.listdir(os.getcwd())):
                tempSetFilenames.add(a)
            
            tempSetDelnames=tempSetFilenames.symmetric_difference(tempSetCellnames)
            for a in tempSetDelnames:
                temptemp=os.path.join(os.getcwd(),a)
                #print(temptemp)
                os.remove(a)
                
            
            #删除完成，清除两个temp集合，返回根目录
            tempSetCellnames.clear()
            tempSetFilenames.clear()
            os.chdir(rootMenu)
    else:
        print('请检查是否存在规范格式的xls文件！')
else:
    print('请将该文件放入存档文件夹运行（包含有level.dat的目录）')


