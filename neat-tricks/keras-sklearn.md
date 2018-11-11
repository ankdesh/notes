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
