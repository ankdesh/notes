## Install ARM NN sdk on android

Ref: [ARM NN SDK installation page](https://developer.arm.com/technologies/machine-learning-on-arm/developer-material/how-to-guides/configuring-the-arm-nn-sdk-build-environment-for-caffe/configuring-the-arm-nn-sdk-build-environment-single-page)

### Install Caffe 
Refer - [Caffe Build](https://github.com/ankdesh/notes/blob/master/howtos/CaffeFromSrc.md)

### Create Android Standalone Toolchain
```sh 
$NDK/build/tools/make_standalone_toolchain.py --arch arm64 --install-dir $MY_TOOLCHAINS/aarch64-linux-android-4.9 --stl gnustl --api 21
```
### Build Compute library

Export the path -
1. $MY_TOOLCHAINS/aarch64-linux-android-4.9/bin
1. Build
```sh
$ CXX=clang++ CC=clang scons arch=arm64-v8a extra_cxx_flags="-fPIC" benchmark_tests=0 validation_tests=0  os=android
```





#### Useful links
- https://github.com/ARM-software/ComputeLibrary/issues/300
- https://github.com/ARM-software/ComputeLibrary/issues/242#issuecomment-338365588
