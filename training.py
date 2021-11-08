"""
@author:zjjyyyk
@function：
"""

from utils import load_txt
import pandas as pd
import os

root_dir = r'C:\Users\DELL\Desktop\共享杯\万例实体数据及字典\文件1_大赛数据实体\train'
info_df = pd.read_csv(os.path.join(root_dir,'train.csv'))

X = []
Y = []

for i in info_df.index:
    pid = info_df.iloc[i,0]
    num = info_df.iloc[i,1]
    ecg = load_txt(os.path.join(root_dir,'train_parsedwaveforms_data',pid+'.txt'))
    II = ecg[1]
    X.append(II)
    Y.append(num)
    print(pid,i)

