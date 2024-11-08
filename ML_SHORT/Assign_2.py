import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

df = pd.read_csv("ML/emails.csv")
df.head()

df.isnull().sum()
df.dropna(inplace=True)
df = df.drop(['Email No.'], axis=1)
X=df.drop(['Prediction'],axis=1)
Y=df['Prediction']
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.3)


knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)

print("KNN Confusion Matrix:\n", confusion_matrix(y_test, y_pred_knn))
cnf = confusion_matrix(y_test, y_pred_knn)
cm = ConfusionMatrixDisplay(confusion_matrix=cnf, display_labels=['Spam', 'Not Spam'])
cm.plot()
plt.show()
# KNN Confusion Matrix:
#  [[953 164]
#  [ 68 367]]
print("KNN Classification Report:",classification_report(y_test, y_pred_knn))
# ----------------------------------------------------
svm = SVC(kernel='linear', probability=True)
svm.fit(X_train, y_train)
y_pred_svm = svm.predict(X_test)


print("SVM Classification Report:",classification_report(y_test, y_pred_svm))
print("SVM Confusion Matrix:\n", confusion_matrix(y_test, y_pred_svm))