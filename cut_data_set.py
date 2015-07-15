__author__ = 'LiGe'
#encoding:utf-8
import csv
reader=csv.reader(file('filter_user.csv', 'rb'))
csvfile = file('9_1_data.csv', 'wb')
writer1=csv.writer(csvfile)
csvfile = file('9_3_data.csv', 'wb')
writer2=csv.writer(csvfile)
csvfile = file('9_7_data.csv', 'wb')
writer3=csv.writer(csvfile)
csvfile = file('9_all_data.csv', 'wb')
writer4=csv.writer(csvfile)
##############################################取样本子集,后三天的作为验证日期，正样本10000个，负样本取100000个，最后对样本子集空间进行预测######################################

#################################取的是样本全集#######################################################################
positive_user_item=set()
num=0
for line in reader:
    if num==0:
        num=num+1
        continue
    time_s=line[5].split(' ')
    time_slot=time_s[0].split('-')
    month=int(time_slot[1])
    day=int(time_slot[2])
    dis_day=(12-month)*30+(19-day)
    if dis_day>=10 and dis_day<=11 :
        writer1.writerow(line)
    if dis_day>=10 and dis_day<=13:
        writer2.writerow(line)
    if dis_day>=10 and dis_day<=17:
        writer3.writerow(line)
    if dis_day>=10 :
        writer4.writerow(line)
    num=num+1
