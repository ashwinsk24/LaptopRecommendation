from sklearn import metrics
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

#load data
laptops = pd.read_csv('laps_test.csv')
data = laptops.drop(['img_link', 'name', 'rating', 'no_of_ratings', 'no_of_reviews','display(in inch)'], axis=1)
categorical_features = ['processor', 'ram', 'storage', 'os']
one_hot = OneHotEncoder()
transformer = ColumnTransformer([('one_hot', one_hot, categorical_features)], remainder='passthrough')
transformed_X = transformer.fit_transform(data)
X = pd.DataFrame(transformed_X.toarray()).iloc[:51, :108]
y = pd.DataFrame(transformed_X.toarray()).iloc[:51, 108]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)
clf = DecisionTreeClassifier(criterion="entropy", max_depth=3, random_state=100, min_samples_leaf=4)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))


