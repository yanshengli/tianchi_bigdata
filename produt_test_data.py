__author__ = 'LiGe'
#encoding:utf-8
import csv
num=0

csvfile = file('test_data_9.csv', 'wb')
writer=csv.writer(csvfile)
for line in csv.reader(file('tianchi_mobile_recommend_train_user.csv','rb')):
    if num==0:
        num=num+1
        continue
    time_s=line[5].split(' ')
    time_slot=time_s[0].split('-')
    month=int(time_slot[1])
    day=int(time_slot[2])
    dis_day=(12-month)*30+(19-day)
    if dis_day<=9:
        writer.writerow(line)