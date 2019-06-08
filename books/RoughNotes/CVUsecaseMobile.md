### Computer Vision use cases for Mobile Phones

----------

#### MLKit Base API - https://developers.google.com/ml-kit/vision/ 
  * Predefined labels or use **AutoML** 
  
| Feature | Base technology | Comments |
|---|---|---|
| Barcode scanning  | Object detection | |
| Face Detection | Object Detection, RNN | Facial Contour, Expressiondetection , video tracking|
| Image labeling  | Object Classification | Identify objects, locations, activities, animal species, products, and more. |
| Landmark detection  | Object Classification | |
| Object Detection and Tracking  |  Object Detection, RNN  | |
| Text Detection  | CNN, RNN | |

----------

#### Google Cloud based Video Analytics https://cloud.google.com/video-intelligence/
  * Classify video using predefined labels or Classify video using custom labels (**AutoML**) 
  * Detect shot changes
  * Detect and track objects
  * Detect and extract text
  * Moderate content
  * Analyze streaming and stored video
  * Video transcription for closed captioning and subtitles

---------

#### Pixel 2 use cases
  * Recognize when music is playing and display the song and artist.
  * This system is trained to recognize the audio fingerprint of over 70,000 songs. This audio recognition happens on the device
  * Portrait Mode effect - The Pixel 2 contains a specialized neural network to recognize what’s important in a photo. “a sensor where every pixel is split into two sub-pixels. This architecture lets us take two pictures out of the same camera lens at the same time: one from the left side of the lens and one through the right. This tiny difference in perspective gives the camera depth perception just like your own two eyes, and it generates a depth map of objects in the image from that."
  * Federated learning - a new kind of machine learning approach that runs directly on mobile devices. 

--------

#### AI Benchmark

| Benchmark  | Neural Network model |  Target HW  |
|---|---|---|
| Object Recognition / Classification   |  MobileNet - V2   |   CPU + NPU + DSP  |
| Object Recognition / Classification  |   Inception - V3   |   CPU + NPU + DSP |
| Face Recognition  |  Inception ResNet V1   |   CPU + NPU + DSP |
| Playing Atari Games  | LSTM RNN   |   CPU only |
| Image Deblurring  |  SRCNN 9-5-5   | DSP + NPU + GPU |
| Image Super-Resolution  | VGG - 19   |   DSP + NPU + GPU |
| Image Super-Resolution |  SRGAN   |   CPU x 2 |
|  Bokeh Simulation  | U-Net   |   CPU only  |
| Semantic Segmentation  |  ICNet, 2X parallel   |   NPU + GPU |
| Photo Enhancement  | ResNet - 12   |   NPU + GPU |
| Memory Limits  |SRCNN 9-5-5   |   NPU + GPU |
