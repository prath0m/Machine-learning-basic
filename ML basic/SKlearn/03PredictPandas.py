from sklearn import tree
import pandas

df= pandas.read_csv('motorvehicle.csv')

feat=df[['cc','seats']]
# print(feat)
labels=df['observation']
# print(labels)

clf= tree.DecisionTreeClassifier()
clf.fit(feat.values,labels.values)

print(clf.predict([[980,4],[10,1],[3000,2]]))
 