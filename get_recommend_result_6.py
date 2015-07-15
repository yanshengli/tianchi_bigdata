__author__ = 'LiGe'
#encoding:utf-8
import csv


def get_result(input_source_result_txt,output_final_result_csv,test_sourc_file_csv):
    result_line_num=set()
    f=open(input_source_result_txt,'r')
    lines=f.readlines()
    num=1
    for line in lines:
        linedata=line[1:-2].strip()
        data=linedata.split('  ')
        #print data[1]
        if float(data[1].strip())>0.78:
            result_line_num.add(num)
        num=num+1
    print len(result_line_num)


    csvfile = file(output_final_result_csv, 'wb')
    writer=csv.writer(csvfile)
    num=1
    suspect_user_item=set()
    for line in csv.reader(file(test_sourc_file_csv, 'rb')):
        if num in result_line_num:
            suspect_user_item.add((line[0],line[1]))
            #writer.writerow((line[0],line[1]))
        num=num+1
    sub_item=set()
    for line in csv.reader(file('tianchi_mobile_recommend_train_item.csv','rb')):
        sub_item.add(line[0])
    count=0
    for k in suspect_user_item:
        if k[1] in sub_item:
            writer.writerow((k[0],k[1]))
            count=count+1
    print count


if __name__=='__main__':
    input_source_result_txt='result9.txt'
    output_final_result_csv='tianchi_mobile_recommendation_predict_9_434.csv'
    test_sourc_file_csv='global_test_data_feature.csv'
    get_result(input_source_result_txt,output_final_result_csv,test_sourc_file_csv)

