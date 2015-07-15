__author__ = 'LiGe'
#encoding:utf-8
import csv
import os
buy=set()
for line in csv.reader(file('./17/17_1_data.csv','rb')):
    if line[5].find('2014-12-17')>=0:
        if line[2]=='4':
            buy.add((line[0],line[1]))
csvfile = file('17_negative.csv', 'wb')
writer=csv.writer(csvfile)

files=os.listdir('./17/')
for filename in files:
    if filename.find('feature')>=0:
        for line in csv.reader(file('./17/'+filename,'rb')):
            if (line[0],line[1]) not in buy:
                writer.writerow(line)

