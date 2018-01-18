## Install Tensorflow from source on Ubuntu 16.04 (CPU)
 
* Install dependencies
```sh
 sudo apt-get install python-numpy python-dev python-pip python-wheel
 sudo pip install six numpy wheel
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
 ```
