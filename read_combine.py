# import os
# import pandas as pd
# path = r'D:\cv-py\pic_1\1_normal\hy_112'
# big_file =[]
# for file in os.listdir(path):
#     big_file.append(pd.read_excel(os.path.join(path,file)))
# writer = pd.ExcelWriter(r'D:/cv-py/pic_1/1_normal/xx.xlsx')
# pd.concat(big_file).to_excel(writer,'sheet1',index=False)
# writer.close()

import os
from os import listdir, getcwd
from os.path import join
import shutil
in_path = r"D:\cv-py\pic_1\2_hot"  #输入需要复制里面内容的文件夹路径
out_pic_Path = r"D:\cv-py\pic_1\2_hot" #将找到的图片放到该路径里
out_xml_path = r"D:\cv-py\pic_1\2_hot"#将找到的xml文件放到该路径里

def get_files(inPath,out_pic_Path,out_xml_path):
    for filepath,dirnames,filenames in os.walk(inPath):   #在多级目录下找文件
        for filename in filenames:
            str1 = filename.split('.')[0]
            str1_1 = filename.split('.')[1]
            if str1_1 == "xml":
                shutil.copy(filepath + "\\" + filename, out_xml_path)
            elif str1_1 == "jpg" or str1_1 == "jpeg" or str1_1 == "JPG" or str1_1 == "JPEG":
                shutil.copy(filepath + "\\" + filename, out_pic_Path) #复制文件
                #shutil.move() 移动文件
            else:
                continue

get_files(in_path,out_pic_Path,out_xml_path)
