__author__ = 'LiGe'
#encoding:Utf-8
import csv
##########################加类标,去用户-商品名，取纯特征文档#############################

def put_on_label(feature_csv,feature_txt_label):
    f=open(feature_txt_label,'w')
    for line in csv.reader(file(feature_csv, 'rb')):
        f.write(line[2]+' '+line[3]+' '+line[4]+' '+line[5]+' '+line[6]
                +' '+line[7]+line[8]
                +' '+line[9]
                +' '+line[10]
                +' '+line[11]
                +' '+line[12]
                +' '+line[13]
                +' '+line[14]
                +' '+line[15]
                +' '+line[16]
                +' '+line[17]
                +' '+line[18]
                +' '+line[19]
                +' '+line[20]
                +' '+line[21]
                +' '+line[22]
                +' '+line[23]
                +' '+line[24]
                +' '+line[25]
                +' '+line[26]
                +' '+line[27]
                +' '+line[28]
                +' '+line[29]
                +' '+line[30]
                +' '+line[31]
                +' '+line[32]
                +' '+line[33]
                +' '+line[34]
                +' '+line[35]
                +' '+line[36]
                +' '+line[37]
                +' '+line[38]
                +' '+line[39]
                +' '+line[40]
                +'\n')

if __name__=="__main__":
    feature_csv='global_test_data_feature.csv'
    feature_txt_lable='test_data_9feature.txt'
    put_on_label(feature_csv,feature_txt_lable)
