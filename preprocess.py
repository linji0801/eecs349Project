# 通用的预处理框架  
  
import pandas as pd  
import numpy as np  
#import scipy as sp  
import matplotlib.pyplot as plt 
import matplotlib
  
# 文件读取  
# def read_csv_file(f, logging=False):  
# 	print("==========读取数据=========")
# 	data=pd.read_csv(f)
# 	if logging:
# 		print(data.head(500))  
# 		print(f, "包含以下列")  
# 		print(data.columns.values)  
# 		print(data.describe())  
# 		print(data.info())  
# 	return data  
sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
data_train = pd.read_csv('sampleData1.csv', header=0)
plt.plot(data_train.click_time)

data_train.ip.plot(kind='kde')
plt.show()


#read_csv_file('/Users/linji0801/Documents/eecs349/finalProject/sampleData1.csv', logging = True)