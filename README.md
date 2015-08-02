# tianchi_bigdata
任务：

[详见天池大数据任务介绍](http://tianchi.aliyun.com/competition/information.htm?spm=0.0.0.0.y1LXeD&raceId=1)

特征（39维）：

	user特征、item特征、user-item特征、全局比例特征
	
数据采样

	采用移动窗口target（17、15、13、11、9）+移动窗口样本采样（1、3、7、全部）

训练数据

	正样本：15000，负样本：130000
	
测试数据

	同样采用移动窗口变换采样，取了3天、5天、9天的做实验，最优提交为9天的，测试样本大小：155万
	
结果划分

	结果最终取置信度0.78,取470条结果(子集结果)，最终f1值：11.46%
	
	排名:25/7200，队伍名：叮当
	
学习模型

	RF

程序架构
	
	combine_feature_txt:混合正负样本特征
	
	cut_data_set.py:按照移动窗口方式，分割数据集
	
	fetch_feature.py：提取特征
	
	fetch_negative_sample:负样本抽样
	
	fetch_sample:提取正、负样本
	
	get_feature_vector_txt_4.py:提取特征向量，去掉用户-商品标示
	
	get_recommend_result_6.py:对最后分类结果取置信度，并得到相应的推荐结果
	
	global_feature.py:提取全局比例特征
	
	product_test_data.py:产生测试数据
	
	classify_user_item.py:训练学习特征，并预测
	
[大赛排名] (http://tianchi.aliyun.com/competition/rankingList.htm?spm=0.0.0.0.OyeBsu&season=0&raceId=1&pageIndex=2)
