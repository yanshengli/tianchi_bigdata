__author__ = 'LiGe'
#encoding:utf-8
##################抽取如下特征,浏览数、收藏数、购物车、购买数、平均活跃天数、最后活跃天数距离最终时间的天数,先不考虑平均活跃天数####

import csv
def fetch_feature(sample_filename,feature_filename,item_brand):
    reader=csv.reader(file(sample_filename, 'rb'))
    csvfile = file(feature_filename, 'wb')
    writer=csv.writer(csvfile)
###################################定义统计变量###########################################
    user_item_click=dict()#(u,i)点击次数
    usr_item_hide=dict()#(u,i)收藏次数
    usr_item_shop_basket=dict()#(u,i)购物车次数
    num=0
    user_item_pair=set()#(u,i)对
    user_basket=dict()#（u）购物车件数
    usr_item_shop=dict()#(用户-item购买次数)
    item_num=dict()
    item_user=dict()
    item_click=dict()
    item_basket=dict()
    item_hide=dict()
    user_buy_brand=dict()
    user_buy_item_brand=dict()
    user_item_num=dict()
    user_brand=dict()
    user_buy=dict()
    user_click=dict()
    user_hide=dict()
    user_item_time=dict()
    user_click_item_brand=dict()
    user_basket_item_brand=dict()
    catogery_buy=dict()
    catogery_click=dict()
    catogery_basket=dict()
    catogery_hide=dict()
    ###################################初始化#############################
    for line in reader:
        if line[5].find('2014-12-17')<0:
            item_brand[line[1]]=line[4]
            user_hide[line[0]]=0
            user_click[line[0]]=0
            user_buy[line[0]]=0
            user_brand[line[0]]=set()
            user_item_num[line[0]]=set()
            user_item_click[(line[0],line[1])]=0
            usr_item_hide[(line[0],line[1])]=0
            usr_item_shop_basket[(line[0],line[1])]=0
            user_item_pair.add((line[0],line[1]))
            usr_item_shop[(line[0],line[1])]=0
            item_num[line[1]]=0
            item_user[line[1]]=set()
            item_click[line[1]]=0
            item_basket[line[1]]=0
            item_hide[line[1]]=0
            user_buy_brand[line[0]]=set()
            user_buy_item_brand[(line[0],item_brand[line[1]])]=0
            user_click_item_brand[(line[0],item_brand[line[1]])]=0
            user_basket_item_brand[(line[0],item_brand[line[1]])]=0
            user_basket[line[0]]=0
            catogery_buy[item_brand[line[1]]]=0
            catogery_click[item_brand[line[1]]]=0
            catogery_basket[item_brand[line[1]]]=0
            catogery_hide[item_brand[line[1]]]=0
            num=num+1
#####################################统计特征############################################
    for line in csv.reader(file(sample_filename, 'rb')):
        if line[5].find('2014-12-17')<0:
            time_s=line[5].split(' ')
            time_slot=time_s[0].split('-')
            month=int(time_slot[1])
            day=int(time_slot[2])
            dis_day=(12-month)*30+(17-day)####间隔时间
            if (line[0],line[1]) not in user_item_time:
                user_item_time[line[0],line[1]]=set()
                user_item_time[line[0],line[1]].add(dis_day)
            else:
                user_item_time[line[0],line[1]].add(dis_day)
            if line[2]=='1':
                #################用户对该商品的点击总数############################
                if (line[0],line[1]) not in user_item_click:
                    user_item_click[(line[0],line[1])]=1
                else:
                    user_item_click[(line[0],line[1])]=1+user_item_click[(line[0],line[1])]
                ####用户点击总数#######
                user_click[line[0]]=user_click[line[0]]+1
                ###############统计点击次数###############################
                #########################统计用户对该商品所对应类型的次数#######################
                user_click_item_brand[(line[0],item_brand[line[1]])]=1+user_click_item_brand[(line[0],item_brand[line[1]])]
                #########################商品对应的种类被点击的次数#############
                catogery_click[item_brand[line[1]]]=catogery_click[item_brand[line[1]]]+1
                ###################商品被点击的总数####################
                item_click[line[1]]=item_click[line[1]]+1
            if line[2]=='2':
                if (line[0],line[1]) not in usr_item_hide:
                    usr_item_hide[(line[0],line[1])]=1
                else:
                    usr_item_hide[(line[0],line[1])]=1+usr_item_hide[(line[0],line[1])]
                #############用户收藏总数################
                user_hide[line[0]]=user_hide[line[0]]+1
                ################商品类型被收藏的次数############
                catogery_hide[item_brand[line[1]]]=catogery_hide[item_brand[line[1]]]+1
                ################商品被加入收藏的次数############
                item_hide[line[1]]=item_hide[line[1]]+1
            if line[2]=='3':
                ################（u,i）加入购物车的次数##############
                if (line[0],line[1]) not in usr_item_shop_basket:
                    usr_item_shop_basket[(line[0],line[1])]=1
                else:
                    usr_item_shop_basket[(line[0],line[1])]=1+usr_item_shop_basket[(line[0],line[1])]
                ############用户加入购物车的总数#######################
                user_basket[line[0]]=user_basket[line[0]]+1
                #########################统计用户对该商品所对应类型的购物车次数###################
                user_basket_item_brand[(line[0],item_brand[line[1]])]=1+user_basket_item_brand[(line[0],item_brand[line[1]])]
                ########################商品种类被加入购物车的次数#####################
                catogery_basket[item_brand[line[1]]]=catogery_basket[item_brand[line[1]]]+1
                ################商品被加入购物车的次数############
                item_basket[line[1]]=item_basket[line[1]]+1
            if line[2]=='4':
                ##############################该用户购买该商品的次数############################
                if (line[0],line[1]) not in usr_item_shop:
                    usr_item_shop[(line[0],line[1])]=1
                else:
                    usr_item_shop[(line[0],line[1])]=usr_item_shop[(line[0],line[1])]+1
                #############用户购买商品的总次数#########################
                user_buy[line[0]]=user_buy[line[0]]+1
                ###########################统计该商品被购买的次数##############################
                item_num[line[1]]=item_num[line[1]]+1
                ###############商品被多少人购买####################
                item_user[line[1]].add((line[0]))
                ##########################种类被购买的次数######################
                catogery_buy[item_brand[line[1]]]=catogery_buy[item_brand[line[1]]]+1
                ################用户购买商品类型的总数############
                user_buy_brand[line[0]].add(item_brand[line[1]])
                ####################用户购买该类型商品种类的数目###########
                user_buy_item_brand[(line[0],item_brand[line[1]])]=1+user_buy_item_brand[(line[0],item_brand[line[1]])]
            #############################用户交互的商品数################
            user_item_num[line[0]].add((line[1]))
            ############################用户交互的商品品牌数####################
            user_brand[line[0]].add(item_brand[line[1]])
#####################################写结果##################################################################
    for k in user_item_pair:
        ####################用户交互的商品数与购买的商品数之比######################
        if user_buy[k[0]]!=0:
            comm_item_ratio=float("%.2f"%(len(user_item_num[k[0]])/user_buy[k[0]]))
        else:
            comm_item_ratio=0
        #################用户交互的商品品牌数与购买的商品品牌数之比##################
        if len(user_buy_brand[k[0]])!=0:
            comm_brand_buy_ratio=float("%.2f"%(len(user_brand[k[0]])/len(user_buy_brand[k[0]])))
        else:
            comm_brand_buy_ratio=0
        ###################该类型商品点击与购买的比例###############
        if catogery_buy[item_brand[k[1]]]!=0:
            catogry_click_buy=float("%.2f"%(catogery_click[item_brand[k[1]]]/catogery_buy[item_brand[k[1]]]))
        else:
            catogry_click_buy=0
        ###################该类型商品加入购物车与购买的比例###############
        if catogery_buy[item_brand[k[1]]]!=0:
            catogry_basket_buy=float("%.2f"%(catogery_basket[item_brand[k[1]]]/catogery_buy[item_brand[k[1]]]))
        else:
            catogry_basket_buy=0
        ####购买该商品所对应的类型占总的购买量的比例########################
        if user_buy[k[0]]!=0:
            buy_catogry_ratio=float("%.2f"%(user_buy_item_brand[(k[0],item_brand[k[1]])]/user_buy[k[0]]))
        else:
            buy_catogry_ratio=0
        ##########################################点击该商品所对应的类型占总的点击量的比例####################
        if user_click[k[0]]!=0:
            click_catogry_ratio=float("%.2f"%(user_click_item_brand[(k[0],item_brand[k[1]])]/user_click[k[0]]))
        else:
            click_catogry_ratio=0
        #########################################购物车该商品所对应的类型占总的购物车的比例######################
        if user_basket[k[0]]!=0:
            basket_catogry_ratio=float("%.2f"%(user_basket_item_brand[(k[0],item_brand[k[1]])]/user_basket[k[0]]))
        else:
            basket_catogry_ratio=0
        ####用户点击购买比例###############
        if user_buy[k[0]]!=0:
            click_buy_user_ratio=float("%.2f"%(user_click[k[0]]/user_buy[k[0]]))
        else:
            click_buy_user_ratio=0
        ######用户-商品对购物车与购买的比例####################
        if usr_item_shop[k]!=0:
            basket_buy_ratio=float("%.2f"%(usr_item_shop_basket[k]/usr_item_shop[k]))
        else:
            basket_buy_ratio=0
        ##########用户-商品点击与购物车的比例######
        if usr_item_shop_basket[k]!=0:
            click_basket=float("%.2f"%(user_item_click[k]/usr_item_shop_basket[k]))
        else:
            click_basket=0
        ##################用户购物车与购买的比例#####################
        if user_buy[k[0]]!=0:
            basket_buy_user_ratio=float("%.2f"%(user_basket[k[0]]/user_buy[k[0]]))
        else:
            basket_buy_user_ratio=0
        #################用户点击与购物车的比例###################
        if user_basket[k[0]]!=0:
            ratio_click_basket=float("%.2f"%(user_click[k[0]]/user_basket[k[0]]))
        else:
            ratio_click_basket=0
        ######################用户收藏与购物的比例#################
        if user_buy[k[0]]!=0:
            ratio_hide_buy=float("%.2f"%(user_hide[k[0]]/user_buy[k[0]]))
        else:
            ratio_hide_buy=0
        ######################该类型商品收藏与购买的比例#################
        if catogery_buy[item_brand[k[1]]]!=0:
            catogry_hide_buy=float("%.2f"%(catogery_hide[item_brand[k[1]]]/catogery_buy[item_brand[k[1]]]))
        else:
            catogry_hide_buy=0
        ###################用户最早接触该物品的时间以及最晚接触该物品的时间#####################
        sort_user_item_time=list(user_item_time[k])
        eraliest_time=sort_user_item_time[-1]
        latest_time=sort_user_item_time[0]

        writer.writerow((k[0],k[1],user_item_click[k],user_click[k[0]],usr_item_hide[k],user_hide[k[0]],\
        usr_item_shop_basket[k],user_basket[k[0]],usr_item_shop[k],user_buy[k[0]],item_num[k[1]],len(item_user[k[1]]),\
        len(user_buy_brand[k[0]]),user_buy_item_brand[(k[0],item_brand[k[1]])],len(user_item_num[k[0]]),len(user_brand[k[0]]),
        user_click_item_brand[(k[0],item_brand[k[1]])],user_basket_item_brand[(k[0],item_brand[k[1]])],catogery_click[item_brand[k[1]]],
        catogery_hide[item_brand[k[1]]],catogery_basket[item_brand[k[1]]],catogery_buy[item_brand[k[1]]],item_click[k[1]],
        item_hide[k[1]],item_basket[k[1]],
        buy_catogry_ratio,click_buy_user_ratio,basket_buy_ratio,click_basket,basket_buy_user_ratio,ratio_hide_buy,
        ratio_click_basket,click_catogry_ratio,basket_catogry_ratio,catogry_click_buy,catogry_basket_buy,
        catogry_hide_buy,comm_item_ratio,comm_brand_buy_ratio,eraliest_time,latest_time))
####################39维特征##################################

if __name__=='__main__':
    item_brand=dict()
    fetch_feature('./17/17_1_data.csv',\
                  './17/17_1_data_feature.csv',item_brand)







