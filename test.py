import pandas as pd
import numpy as np

sample1 = pd.read_excel('Clouds-+18Competition.xlsx', usecols= "C,D,F,I,K,L,M,O")

def RT_reader(row):
    RTstr = sample1.iloc[row , 3]
    RTlist = [int(i) for i in RTstr.split(",")]
    return RTlist

def RT_mean_level(row):
    RTlist = RT_reader
    return (sum(RTlist)) / (len(RTlist))

RTMean = []

rows = len(sample1)

sum = RT_mean_level(0)
n = 1
m = 0
for i in range (1 , rows):
    if bool(sample1.iloc[i, 7]) is False:
        sum = sum + RT_mean_level(i)
        n = n+1
    else:
        RTMean.append(sum/n)
        n = 1
        m = m+1
        sum = RT_mean_level(i)
RTMean.append(sum/n)

print(RTMean)
print(len(RTMean))