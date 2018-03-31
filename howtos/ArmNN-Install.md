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
- $MY_TOOLCHAINS/aarch64-linux-android-4.9/bin
- Build
```sh
$ CXX=clang++ CC=clang scons arch=arm64-v8a extra_cxx_flags="-fPIC" benchmark_tests=0 validation_tests=0  os=android
```
- If you want to support OpenCL for your Arm Mali GPU, add these arguments to the SCons command:
```sh
opencl=1 embed_kernels=1
```
- If you want to support NEON, add this argument to your SCons command:
```sh
neon=1  
```



#### Useful links
- https://github.com/ARM-software/ComputeLibrary/issues/300
- https://github.com/ARM-software/ComputeLibrary/issues/242#issuecomment-338365588
