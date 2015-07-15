__author__ = 'LiGe'
#encoding:utf-8
import csv
global_user_feature=dict()

for line in csv.reader(file('9_all_data.csv','rb')):
    global_user_feature[(line[0],line[1])]=line[25:]

csvfile = file('gloabal_9_1_data.csv', 'wb')
writer=csv.writer(csvfile)
for line in csv.reader(file('9_1_data.csv','rb')):
    k=global_user_feature[(line[0],line[1])]
    writer.writerow((line[0],line[1],line[2],line[3],
                     line[4],line[5],line[6],line[7],
                     line[8],line[9],line[10],line[11],
                     line[12],line[13],line[14],line[15],
                     line[16],line[17],line[18],line[19],
                     line[20],line[21],line[22],line[23],
                     line[24],k[0],k[1],k[2],k[3],k[4],k[5],
                     k[6],k[7],k[8],k[9],k[10],k[11],k[12],
                     k[12],k[13],k[14],k[15]
                     ))