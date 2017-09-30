## Setting up docker based Development environtments

#### Ubutnu-base 
```sh
docker run -it -v <devel-dir>:/home/ankdesh  ankdesh-custom
```

#### Tensorflow
```sh
docker run -it -v /home/ankdesh/explore:/notebooks -p 8888:8888 gcr.io/tensorflow/tensorflow:latest
```
