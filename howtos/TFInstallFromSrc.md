## Install Tensorflow from source on Ubuntu 16.04 (CPU)
 
* Install dependencies
```sh
 sudo apt-get install python-numpy python-dev python-pip python-wheel
 sudo pip install six numpy wheel
 ```
 (Optional) For GPU, install Cuda>7.0 and Cudnn>3.0 and
 ```sh
 sudo apt-get install libcupti-dev
 ```
 
 
 * Install Bazel
 ```
 sudo apt-get install openjdk-8-jdk
 echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
 curl https://bazel.build/bazel-release.pub.gpg | sudo apt-key add -
 sudo apt-get update && sudo apt-get install bazel
 ```
 
 * Install Tensorflow
 ```
 git clone https://github.com/tensorflow/tensorflow
 cd tensorflow
 ./configure
 bazel build --config=opt //tensorflow/tools/pip_package:build_pip_package
 bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg
 sudo pip install /tmp/tensorflow_pkg/tensorflow-1.5.0rc0-cp27-cp27mu-linux_x86_64.whl
 ```
