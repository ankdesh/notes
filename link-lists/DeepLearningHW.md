## Deep Learning Hardware

### Inferencing Hardware
*These hardware are specialized to accelerate inferencing on already trained Deep learning models.*

#### Research papers studying impact of precision for Deep Learning Models.
* [Training deep neural networks with low precision multiplications](https://arxiv.org/abs/1412.7024) - One of the initial papers which systematically studied the effect of precision on inferencing for DNNs.
* <a name="Sanghon"></a> [Deep Compression: Compressing Deep Neural Networks with Pruning, Trained Quantization and Huffman Coding](https://arxiv.org/pdf/1510.00149v5.pdf) - Arguably best paper to introduce systemtatic pipeline to prune unncessary weights, Quatization and applying clustering of weights to reduce the amount of computations for CNNs.

##### Papers for hardware specialized for accelerating CNN models  
* [EIE: Efficient Inference Engine on Compressed Deep Neural Network](https://arxiv.org/abs/1602.01528) - Implementation of hardware for CNN accelaration based on ideas from [this paper](#Sanghon)

##### Papers for hardware specialized for accelerating LSTM models
* [ESE: Efficient Speech Recognition Engine with Sparse LSTM on FPGA](https://arxiv.org/abs/1612.00694) - FPGA implementation of the hardware for accelerating LSTM models for Speech Recognition benchmarks.

### Learning Hardware
*These harware are used to accelerate learning phase for Deep learning models*
