import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as tts
from sklearn.tree import DecisionTreeClassifier as tree
from sklearn.tree import plot_tree as treeplt
from sklearn.metrics import confusion_matrix as cm
from sklearn.metrics import accuracy_score as score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import LabelEncoder as le
df = pd.read_csv('heartn.csv - heartn.csv.csv')
X = df[['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
'exang', 'oldpeak', 'slope', 'ca', 'thal']]
df['target'] = le().fit_transform(df['target'])
y = df['target']
X_train,X_test,y_train,y_test = tts(X,y,train_size=0.8,random_state=0)
model = tree(max_depth=1)
model.fit(X_train,y_train)
plt.figure()
treeplt(model,filled=True)
plt.title('Decision tree on Heart dataset')
plt.show()
y_pred = model.predict(X_test)
print(f'Confusion Matrix: \n{cm(y_test,y_pred)}')
print(f'Accuracy Score: {score(y_test,y_pred)}')
print(f'Recall Score: {recall_score(y_test,y_pred,pos_label=1)}')
print(f'Specificity: {recall_score(y_test,y_pred,pos_label=0)}')
print(f'Precision Score: {precision_score(y_test,y_pred)}')
print(f'F1 Score: {f1_score(y_test,y_pred)}')
y_proba = model.predict_proba(X_test)
fpr,tpr,thresh = roc_curve(y_test,y_proba[:,1])
plt.plot(fpr,tpr,linestyle='-',color='pink')
plt.title('ROC CURVE')
plt.xlabel('False Postive Rate')
plt.ylabel('True Positive rate')
plt.show()
print(f'AUC Score: {roc_auc_score(y_test,y_proba[:,1])}')
