## Setting up docker based Development environtments

#### Ubutnu-base 
```sh
docker run -it -v <devel-dir>:/home/ankdesh  ankdesh-custom
```

#### Tensorflow
```sh
nvidia-docker run --rm --name tf-gpu -it -v /home/ankdesh/explore/LearnTry:/notebooks  -p 8888:8888 -p 6006:6006 tf-latest-gpu-py3.4
```
#### Cuda-jupyter
```sh
nvidia-docker run --rm --name cuda8.gpu -it -v /home/ankdesh/explore/LearnTry:/notebooks  -v /home/ankdesh/installed/virtualenvs:/virtualenvs -p 8888:8888 cuda8.jupyter
```
