
# %%
#===A Simple Machine Learning Project===
#  ---Music Prediction---

## Importing Packages
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

## Loading Dataset
music_data = pd.read_csv('music.csv')
music_data
# %%
## Splitting the dataset (input - X and output - Y)
X = music_data.drop(columns = ['genre'])
Y = music_data['genre'] 

print(f"Imput dataset:\n {X}\n\n Output dataset:\n{Y}")
# %%
## modeling 
model = DecisionTreeClassifier()
model.fit(X,Y)
predictions = model.predict([[21, 1], 
                             [22, 0]])
predictions
# %%
## Measuring the accuracy of models
## Training and Testing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)

model.fit(X_train, Y_train)
predictions = model.predict(X_test)