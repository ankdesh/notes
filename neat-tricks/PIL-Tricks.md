# PIL (Python Image Library) snippets

* Importing Image
```python
from PIL import Image
```

* Read Jpg Image to numpy buffer 
```python
readImage = Image.open(open(filename))
npImg = np.array(readImage)
```

* Display single image from numpy buffer
```python
pl.imshow(Image.fromarray(X))
```

* Display image and other formats in ipython notebook
https://ipython.org/ipython-doc/2/api/generated/IPython.core.display.html
e.g for image
```python
display(Image(filename=imageName)
```

* Display images horizontally
```python
import matplotlib.pyplot as plt
from PIL import Image
imgs = [] # Stores name of files  
f,ax = plt.subplots(1,5, figsize=(15,15))
for i in range(5):
    ax[i].imshow(Image.open(imgs[i]))
plt.show() # or display.display(plt.gcf()) if you prefer
```

* Display montage of image files
```python
def createMontage (images, widthMontage = 1000, heightMontage = 1000):
    if isinstance(images, list):
        images = np.array(images)    
    
    imgH = images.shape[1]
    imgW = images.shape[2]
    
    numImgsPerDim = int(np.ceil(np.sqrt(images.shape[0])))
    smallImgW = widthMontage // numImgsPerDim
    smallImgH = heightMontage // numImgsPerDim
    
    if len(images.shape) == 4 and images.shape[3] == 3: # RGB images
        montage = Image.new(mode = 'RGB', size = (widthMontage, heightMontage))
        
        smallImg = None
        for i in range(numImgsPerDim):
            for j in range(numImgsPerDim):
                imageNum = i * numImgsPerDim + j
                ratioDownSampleH = imgH // smallImgH
                ratioDownSampleW = imgW // smallImgW
                smallImg = Image.fromarray(images[imageNum,:,:,:]).resize(size = (smallImgW, smallImgH))
                montage.paste (smallImg, box = (i*smallImgH,j*smallImgW))
        
        return montage
```

* Display images in 3x3 subplots with true and predicted labels
```python
def plot_images(images, cls_true, cls_pred=None):
    assert len(images) == len(cls_true) == 9
    
    # Create figure with 3x3 sub-plots.
    fig, axes = plt.subplots(3, 3)
    fig.subplots_adjust(hspace=0.3, wspace=0.3)

    for i, ax in enumerate(axes.flat):
        # Plot image.
        ax.imshow(images[i].reshape(img_shape), cmap='binary')

        # Show true and predicted classes.
        if cls_pred is None:
            xlabel = "True: {0}".format(cls_true[i])
        else:
            xlabel = "True: {0}, Pred: {1}".format(cls_true[i], cls_pred[i])

        ax.set_xlabel(xlabel)
        
        # Remove ticks from the plot.
        ax.set_xticks([])
        ax.set_yticks([])
        
    # Ensure the plot is shown correctly with multiple plots
    # in a single Notebook cell.
    plt.show()
```

