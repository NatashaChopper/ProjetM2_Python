# -*- coding: utf-8 -*-

#test pour découvrir sklearn 

import pandas as pd
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
#on lit les data et on retire la colonne ID
data = pd.read_csv('./iris/Iris.csv',header=0)
data.drop('Id', axis=1, inplace=True)

#row indexer & column indexer => pour les features, on veut tout, sauf la dernière valeur
#X = data.iloc[:,:-1].values
#avec la nouvelle maj c'est mieux d'utiliser to_numpy
X = data.iloc[:,:-1].to_numpy()
#on peut aussi faire comme ça
#X = data.iloc['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm']

#labels
#y = data.iloc[:,-1]
y = data['Species']

# Test size specifies how much of the data you want to set aside for the testing set. 
# Random_state parameter is just a random seed we can use.
# You can use it if you'd like to reproduce these specific results.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=27)

#on instancie les modèles
SVC_model = SVC()
# KNN model requires you to specify n_neighbors,
# the number of points the classifier will look at to determine what class a new point belongs to
KNN_model = KNeighborsClassifier(n_neighbors=5)


#to train
SVC_model.fit(X_train, y_train)
KNN_model.fit(X_train, y_train)

#on peut prédire maintenant
SVC_prediction = SVC_model.predict(X_test)
KNN_prediction = KNN_model.predict(X_test)

# Accuracy score is the simplest way to evaluate
print(accuracy_score(SVC_prediction, y_test))
print(accuracy_score(KNN_prediction, y_test))
# But Confusion Matrix and Classification Report give more details about performance
print(confusion_matrix(SVC_prediction, y_test))
print(classification_report(KNN_prediction, y_test))

#plot le modèle SVC
plt.scatter(y_test, SVC_prediction)
plt.xlabel("True Values")
plt.ylabel("Predictions")