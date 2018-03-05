# PIL (Python Image Library) snippets

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
* Display single image from buffer
```python
pl.imshow(Image.fromarray(X))
```

* Display image and other formats in ipython notebook
https://ipython.org/ipython-doc/2/api/generated/IPython.core.display.html
e.g for image
```python
display(Image(filename=imageName)
```