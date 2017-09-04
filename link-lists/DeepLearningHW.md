## Deep Learning Hardware

### Inferencing Hardware
*These hardware are specialized to accelerate inferencing on already trained Deep learning models.*

##### Papers about impact of precision for Deep Learning Models.
* [Training deep neural networks with low precision multiplications](https://arxiv.org/abs/1412.7024) - One of the initial papers which systematically studied the effect of precision on inferencing for DNNs.

* [Efficient Processing of Deep Neural Networks: A Tutorial and Survey](https://arxiv.org/abs/1703.09039) Best survey paper for undestanding various aspects of Deep learning, with special emphasis on hardware design choices. Highly recommended paper for anyone who has minimal knowledge of Deep learning and looking for references for going deeper and more exhaustive about the topic.

* <a name="Sanghon"></a> [Deep Compression: Compressing Deep Neural Networks with Pruning, Trained Quantization and Huffman Coding](https://arxiv.org/pdf/1510.00149v5.pdf) - Arguably best paper to introduce systemtatic pipeline to prune unncessary weights, Quatization and applying clustering of weights to reduce the amount of computations for CNNs.

##### Papers for hardware specialized for accelerating CNN models  
* [EIE: Efficient Inference Engine on Compressed Deep Neural Network](https://arxiv.org/abs/1602.01528) - Implementation of hardware for CNN accelaration based on ideas from [this paper](#Sanghon)

##### Papers for hardware specialized for accelerating LSTM models
* [ESE: Efficient Speech Recognition Engine with Sparse LSTM on FPGA](https://arxiv.org/abs/1612.00694) - Arguably best paper for describing pruning and quatization effects on LSTM model for Speech recognition. Also introduces FPGA implementation based on the optimizations by removing redundant weights.

* [Recurrent Neural Networks Hardware Implementation on FPGA](https://arxiv.org/pdf/1511.05552.pdf) - FPGA Implementation for RNNs trained for a character level language model

#### Videos and others resources
* [Stanford CS231n - Lecture 15 | Efficient Methods and Hardware for Deep Learning](https://www.youtube.com/watch?v=eZdOkDtYMoo&index=15&list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv) In this invited talk, Sanghon describes the different ideas like pruning, quatization, clustering etc used in creation of efficient hardware for deep learning models.

* [Toward Efficient Deep Neural Network Deployment: Deep Compression and EIE](https://www.youtube.com/watch?v=CrDRr2fxbsg) Another interesting talk by Songhan.


### Learning Hardware
*These harware are used to accelerate learning phase for Deep learning models*
