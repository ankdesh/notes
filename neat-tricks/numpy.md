# Numpy Recipes

* Convert a ndarray of (num_features, image_size, image_size) to (num_features, image_size * image_size) of float32 type
```python
dataset.reshape((-1, image_size * image_size)).astype(np.float32)
```

* Create a one hot encoding for features from range (0-num_labels) to vector of length num_length. Mapping value x -> vec of len num_length with xth value as 1.0.
Here labels is a nparray of feature vector of length (num_features) with range (0-num_labels) each.
```python
(np.arange(num_labels) == labels[:,None]).astype(np.float32)
```

* Change size of imshow window and plotting downsampled array - a 
```python
fig = plt.figure(figsize=(2, 2))
plt.imshow(asd[::2,::2])
```

* Logical operations on masks
```python
mod_mask = ((my_vector % 7) == 0)
pos_mask = (my_vector > 0)
combined_mask = np.logical_and(mod_mask, pos_mask)
```

* Sum across axis
```python

bsd = np.arange(30).reshape((2,3,5))
print (bsd)
[[[ 0  1  2  3  4]
  [ 5  6  7  8  9]
  [10 11 12 13 14]]

 [[15 16 17 18 19]
  [20 21 22 23 24]
  [25 26 27 28 29]]]

print (bsd.shape)
(2, 3, 5)

print (bsd.ndim)
3

print (bsd.size)
30

print (bsd.dtype)
int64

print (bsd.sum())
435

print (bsd.sum(axis=0))
print (bsd.sum(axis=0).shape)
[[15 17 19 21 23]
 [25 27 29 31 33]
 [35 37 39 41 43]]
(3, 5)

print (bsd.sum(axis=1))
print (bsd.sum(axis=1).shape)
[[15 18 21 24 27]
 [60 63 66 69 72]]
(2, 5)

print (bsd.sum(axis=2))
print (bsd.sum(axis=2).shape)
[[ 10  35  60]
 [ 85 110 135]]
(2, 3)
```
```sh
If we gives (axis = 0), it eliminates 0 th axis and results in matrix (3,5) i.e. it sums over "channel" axis. 
In case (axis = 1), it sums over "rows" axis i.e. find the sum of rows in each channel. It eliminates 1st axis and resulting shape is (2,5) 
In case of axis=2, it sums over elements in the rows and results in size of (2,3) 
```
