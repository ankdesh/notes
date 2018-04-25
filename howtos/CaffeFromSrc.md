## Install Caffe from source on Ubuntu 16.04 (CPU/GPU)

### Dependencies
```sh
$ sudo apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler
$ sudo apt-get install --no-install-recommends libboost-all-dev
$ sudo apt-get install the python-dev
$ sudo apt-get install libgflags-dev libgoogle-glog-dev liblmdb-dev
$ sudo apt-get install libopenblas-dev libatlas-base-dev
```

### Make Config file
```sh
$ cp Makefile.config.example Makefile.config
```

### Fix hdf5 issue from 
https://stackoverflow.com/questions/37007495/caffe-didnt-see-hdf5-h-when-compiling
```
In your Makefile.config try to append /usr/include/hdf5/serial/ to INCLUDE_DIRS:

--- INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include
+++ INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include /usr/include/hdf5/serial/
and rename hdf5_hl and hdf5 to hdf5_serial_hl and hdf5_serial in the Makefile:

--- LIBRARIES += glog gflags protobuf boost_system boost_filesystem m hdf5_hl hdf5
+++ LIBRARIES += glog gflags protobuf boost_system boost_filesystem m hdf5_serial_hl hdf5_serial
```

### Build Caffe
```sh
$ make all -j4
```
