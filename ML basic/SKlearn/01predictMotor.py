#pip install scikit-learn
from sklearn import tree

#features-> cc,seats
features = [[800,5],[1200,5],[150,2],[7500,2],[4500,3],[125,2],[1500,5]]

labels = ['car','car','motor cycle','truck','truck','motor cycle','car']

clf=tree.DecisionTreeClassifier()
clf.fit(features,labels)

print(clf.predict([[110,2],[1700,5]]))

'''
walking 0/1
cycling 0/1
outdoor sport 0/1
wake time 4/5/6/7/8
totalsleeptime 4/5/6/7/8/9
nonveg 0/1
regularalcohol 0/1
age 23/45
gender 1/2/3

Observation yes/no
'''