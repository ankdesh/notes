# Pandas Recipes

* Find unique values in a Series, find number of unique values
```python
df['Class'].unique()
df['Class'].nunique()
```

* Create correlation plots with seaborn and pandas
```py
import seaborn as sns
sns.pairplot(df, hue="species")
```

* Convert categorial series to one hot encoded target
```py
target_names = df['species'].unique()
print (target_names)
Out[24]:
array(['setosa', 'versicolor', 'virginica'], dtype=object)

target_dict = {n:i for i, n in enumerate(target_names)}
print (target_dict)
Out[25]:
{'setosa': 0, 'versicolor': 1, 'virginica': 2}

y= df['species'].map(target_dict)
print (y.head())

Out[26]:
0    0
1    0
2    1
3    0
4    2
Name: species, dtype: int64

from tensorflow.keras.utils import to_categorical
from tensorflow.keras.utils import to_categorical

y_cat = to_categorical(y)

Out[33]:
array([[1., 0., 0.],
       [1., 0., 0.],
       [1., 0., 0.],
       [1., 0., 0.],
       [1., 0., 0.],
       [1., 0., 0.],
       [1., 0., 0.],
       [1., 0., 0.],
       [1., 0., 0.],
       [1., 0., 0.]], dtype=float32)
 ```
 
 
