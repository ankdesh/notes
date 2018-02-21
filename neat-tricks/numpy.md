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
