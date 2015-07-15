__author__ = 'LiGe'
#encoding:utf-8
i=9
f1=open('combine_txt_positive_feature.txt','wb')
while (i<18):
    filename='2014-12-'+str(i)
    filename=filename+'_positive_user_item_feature.txt'
    f=open(filename,'r')
    lines=f.readlines()
    for line in lines:
        f1.write(line)
    i=i+1