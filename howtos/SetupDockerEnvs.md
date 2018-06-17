## Setting up docker based Development environtments

#### Ubutnu-base 
```sh
docker run -it -v <devel-dir>:/home/ankdesh  ankdesh-custom
```

#### Cuda with Display set
```sh
nvidia-docker run --rm --name tf-gpu -it -e DISPLAY=$DISPLAY  -v /tmp/.X11-unix:/tmp/.X11-unix -v /root/.Xauthority:/root/.Xauthority:rw -v /home/ankdesh/explore/:/home/ankdesh/explore  -v /home/ankdesh/virtualenvs:/home/ankdesh/virtualenvs -v /home/ankdesh/.ssh:/home/ankdesh/.ssh -p 8888:8888  ankdesh/tf-devel-gpu:latest
```

#### Tensorflow
```sh
nvidia-docker run --rm --name tf-gpu -it -v /home/ankdesh/explore/LearnTry:/notebooks  -p 8888:8888 -p 6006:6006 tf-latest-gpu-py3.4
```
#### Cuda-jupyter
```sh
nvidia-docker run --rm --name cuda8.gpu -it -v /home/ankdesh/explore/LearnTry:/notebooks  -v /home/ankdesh/installed/virtualenvs:/virtualenvs -p 8888:8888 cuda8.jupyter
```

### Cuda bash with python-2.7 and python-3.4
```sh
nvidia-docker run --rm --name cuda8.bash -it -v /home/ankdesh/explore/kaggle-cdiscount/:/home/ankdesh/code  -v /home/ankdesh/installed/virtualenvs:/home/ankdesh/virtualenvs -v /media/ssd/datasets/cdiscount/:/home/ankdesh/dataset -p 8888:8888 ankdesh/cuda8.bash:latest
```

