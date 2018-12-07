import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import math
from sklearn.preprocessing import scale
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import xgboost as xgb
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import make_scorer
from sklearn.metrics import f1_score
from sklearn.metrics import *

data=pd.read_csv('final_dataset.csv')

y_all=data['FTR']

features=['HTPTN','ATPTN','HGSTN','HGCTN','AGSTN','AGCTN','histhome','histaway']

x_all=data[features]

x_train=x_all[0:2660]
x_test=x_all[2661:]

y_train=y_all[0:2660]
y_test=y_all[2661:]

forest_clf = RandomForestClassifier(n_estimators = 100, max_depth = 10, random_state = 1)
forest_clf.fit(x_train, y_train)
y_pred = forest_clf.predict(x_test)
print("ACCURACY:")
print(accuracy_score(y_test, y_pred, normalize=True, sample_weight=None))

teams = {}
for i in data.groupby('HomeTeam').mean().T.columns:
	teams[i] = 0
for i in range(len(y_pred)):
	if y_pred[i] == 'H':
		teams[data.loc[2660+i, 'HomeTeam']] += 3
	if y_pred[i] == 'A':
		teams[data.loc[2660+i, 'AwayTeam']] += 3
	if y_pred[i] == 'D':
		teams[data.loc[2660+i, 'HomeTeam']] += 1
		teams[data.loc[2660+i, 'AwayTeam']] += 1

sorted_teams = sorted( ((value,key) for (key,value) in teams.items()), reverse = True)
print sorted_teams
