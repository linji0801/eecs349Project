import numpy as numpy
import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib
import sklearn
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('/Users/linji0801/Documents/eecs349/finalProject/sampleData1.csv', header=0)

y = df.attributed_time
x = df.drop('attributed_time', axis=1)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25,random_state = 30)

clf = RandomForestClassifier(n_estimators=1000, random_state=30)
clf = clf.fit(x_train, y_train)
#clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3, min_samples_leaf=5)
#fit(x_train,y_train)
print("准确率为：{:.2f}".format(clf.score(x_test,y_test)))

#scores = cross_validation.cross_val_score(clf,x,y,cv=10)
#print ("accuracy: {:.2f}".format(clf.score(x_test,y_test)))
#clf.feature_importances_