# tianchi_bigdata
任务：

	详见：http://tianchi.aliyun.com/competition/information.htm?spm=0.0.0.0.y1LXeD&raceId=1

特征（39维）：

	user特征、item特征、user-item特征、全局比例特征
	
数据采样

	采用移动窗口target+移动窗口样本采样
	
训练数据

	正样本：15000，负样本：130000
	
测试数据

	同样采用移动窗口变换采样，取了3天、5天、9天的做实验，最优提交为9天的，测试样本大小：155万
	
结果划分

	结果最终取置信度0.78,取470条结果(子集结果)，最终f1值：11.04%，排名:25/7200，队伍名：叮当，排名详见http://tianchi.aliyun.com/competition/rankingList.htm?spm=0.0.0.0.OyeBsu&season=0&raceId=1&pageIndex=2
	
学习模型
	RF


