"""
@author:zjjyyyk
@function：
"""

import matplotlib.pyplot as plt
import numpy as np

def load_txt(fpath):
    ecg = []
    with open(fpath, 'r') as f:
        r = f.read()
    s = r.split('^')
    s = s[:-1]
    for part in s:
        part = part.replace('\n', '').strip()
        part_name = part.split(':')[0]
        datastr = part.split(':')[1].replace('200', '0')
        data = list(map(eval, datastr.split(' ')))
        ecg.append(data)
    ecg = np.array(ecg)
    print(ecg.shape)
    return ecg

def plot12_ecg(ecg):
    plt.figure(figsize=(18,10))
    for i in range(12):
        plt.subplot(12,1,i+1)
        plt.plot(ecg[i])
        plt.ylabel(part_name_list[i])
    plt.show()

if __name__ == '__main__':
    fpath = '1500006.txt'
    part_name_list = 'I,II,III,aVR,aVL,aVF,V1,V2,V3,V4,V5,V6'.split(',')
    ecg = load_txt(fpath)
    print(list(ecg[1]))
    plot12_ecg(ecg)
