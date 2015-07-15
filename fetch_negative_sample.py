__author__ = 'LiGe'
#encoding:utf-8
import csv
import random

num=1
csvfile = file('sample_17_negative_user.csv', 'wb')
writer=csv.writer(csvfile)
for line in csv.reader(file('17_negative.csv','r')):
    if num%200==0:
        writer.writerow(line)
    num=num+1
print num