# Keras and Sklearn based pipeline and tricks

* Sample pipeline using Keras and Sklearn
```python
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam, SGD
from tensorflow.keras.utils import to_categorical

from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold, cross_val_score

# Read data
df = pd.read_csv('file.csv')
X = data[['sqft','bdrms','age']].values # Can also use data.drop('price').values
Y = data['price'].values
print (X.shape, Y.shape)

# Split Train/Test data
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2)

y_cat_train = to_categorical(y_train)

def getModel():
    model = keras.models.Sequential()
    model.add(Dense(units=100, input_shape=(20,), activation='relu'))
    model.add(Dense(units=1, activation='sigmoid'))
    model.compile(Adam(lr=0.1), loss='binary_crossentropy',metrics = ['accuracy'])
    model.summary()
    return model
    
model = KerasClassifier(build_fn=getModel)
model.fit(X_train, y_train, epochs=20, validation_split=0.1)

y_pred = model.predict(X_test)

y_test_class = np.argmax(y_test, axis=1)
y_pred_class = np.argmax(y_pred, axis=1)

print (accuracy_score(y_test_pred,Y_test_class).round(2))
print (classification_report(y_test_pred,Y_test_class))

```
* Plot training and validation history after train
```py
plt.plot(h.history['acc'])
plt.plot(h.history['val_acc'])
plt.legend(['Training', 'Validation'])
plt.title('Accuracy')
plt.xlabel('Epochs')
```


* Generating various reports for classification tasks
```py
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_martix

print(classification_report(y_test_class, y_pred_class))

              precision    recall  f1-score   support

           0       1.00      1.00      1.00         8
           1       0.90      1.00      0.95         9
           2       1.00      0.92      0.96        13

   micro avg       0.97      0.97      0.97        30
   macro avg       0.97      0.97      0.97        30
weighted avg       0.97      0.97      0.97        30

confusion_matrix(y_test_class, y_pred_class)
Out[42]:
array([[ 8,  0,  0],
       [ 0,  9,  0],
       [ 0,  1, 12]])
```

* Rescaling all columns to normal distribution (mean=0, var=1) 
```py
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()

for i, col in enumerate(df.columns):
    df[col+'_ss'] = ss.fit_transform(df[[col]]) 

####### OR ##########

from sklearn.preprocessing import scale
X = scale(df.drop('class', axis=1).values)
```

* Doing hyperparameter search for Learning rate and plotting results
```py
#### Details at https://github.com/ankdesh/LearnTry-ML/blob/master/Keras/zero_to_deep_learning_udemy/course/5 Gradient Descent.ipynb #####

dflist = []

learning_rates = [0.01, 0.05, 0.1, 0.5]

for lr in learning_rates:
    model = Sequential()
    model.add(Dense(1, input_shape=(4,), activation='sigmoid'))
    model.compile(loss='binary_crossentropy',
                  optimizer=SGD(lr=lr),
                  metrics=['accuracy'])
    h = model.fit(X_train, y_train, batch_size=16, verbose=0, epochs=10)
    
    dflist.append(pd.DataFrame(h.history, index=h.epoch))

historydf = pd.concat(dflist, axis=1)
metrics_reported = dflist[0].columns
idx = pd.MultiIndex.from_product([learning_rates, metrics_reported],
                                 names=['learning_rate', 'metric'])

historydf.columns = idx
ax = plt.subplot(211)
historydf.xs('loss', axis=1, level='metric').plot(ylim=(0,1), ax=ax)
plt.title("Loss")

ax = plt.subplot(212)
historydf.xs('acc', axis=1, level='metric').plot(ylim=(0,1), ax=ax)
plt.title("Accuracy")
plt.xlabel("Epochs")

plt.tight_layout()
``` py
