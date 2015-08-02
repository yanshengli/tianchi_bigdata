__author__ = 'LiGe'
#encoding:utf-8
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
import numpy as np
f = open("train_sample.txt")
f.readline()
data = np.loadtxt(f)
X = data[:, :-1]  # select columns 1 through end
y = data[:, -1]   # select column 0, the stock price
print X
print y
print 'start train'

clf2 = RandomForestClassifier(n_estimators=100)
#clf2=GradientBoostingClassifier()
clf2.fit(X,y)
#clf2 = LogisticRegression().fit(X, y)
print clf2.classes_
f1=open("test_data_9feature.txt")
data1=np.loadtxt(f1)
X_new=data1[:,:]
print 'testing data is ok'
result=clf2.predict_proba(X_new)
print 'output result'
print result
f_result=open('result9.txt','w')
for i in range(0,len(result)):
    f_result.write(str(result[i])+'\n')

