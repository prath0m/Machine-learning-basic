from sklearn import tree

x = [1],[9],[13],[26]
y=['no umbrella','umbrella','raincoat','stay home']

clf=tree.DecisionTreeClassifier()
clf.fit(x,y)

print(clf.predict([3]))

'''
cloud 1/2/3/4
wind 
thunderstorms
rain
'''