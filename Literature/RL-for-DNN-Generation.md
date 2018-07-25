## Literature survey for neural network generation using Deep Reinforment Learning


| Title                                                                                   | Summary                                                                                                                                                                                                                                                                                                                                                                  | Differentiation point                             | Link                             | Affiliations                      | Comments                                                                                                                                                         | arxiv Date |
|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|----------------------------------|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| Designing Neural Network Architectures using Reinforcement Learning                     | The learning agent is trained to sequentially choose CNN layers using Q-learning with an ϵ-greedy exploration strategy and experience replay. The agent explores a large but finite space of possible architectures and iteratively discovers designs with improved performance on the learning task.                                                                    | * Generation of CNN Models only. No pruning       | https://arxiv.org/abs/1611.02167 | MIT                               | * Tabular Q learning based approach                                                                                                                              | Nov, 2016  |
| Neural Architecture Search with Reinforcement Learning                                  | In this paper, we use a recurrent network to generate the model descriptions of neural networks and train this RNN with reinforcement learning to maximize the expected accuracy of the generated architectures on a validation set.                                                                                                                                     | * Generation of CNN Models only. No pruning       | https://arxiv.org/abs/1611.01578 | Google                            | * Deep reinforcement learning with  policy gradient                                                                                                              | Feb, 2017  |
| Learning Transferable Architectures for Scalable Image Recognition                      | The key contribution of this work is the design of a new search space (the "NASNet search space") which enables transferability.                                                                                                                                                                                                                                         | * Generations of DNN models. No pruning           | https://arxiv.org/abs/1707.07012 | Google Brain                      | * Deep reinforcement learning with  policy gradient* NASNet                                                                                                      | Dec, 2017  |
| Efficient Neural Architecture Search via Parameter Sharing                              | a controller learns to discover neural network architectures by searching for an optimal subgraph within a large computational graph. The controller is trained with policy gradient to select a subgraph that maximizes the expected reward on the validation set.                                                                                                      | * Generation of CNN Models only. No pruning       | https://arxiv.org/abs/1802.03268 | Google Brain                      | * Makes search faster by order of magnitudes                                                                                                                     |            |
| N2N Learning: Network to Network Compression via Policy Gradient Reinforcement Learning | Our approach takes a larger `teacher' network as input and outputs a compressed `student' network derived from the `teacher' network. In the first stage of our method, a recurrent policy network aggressively removes layers from the large `teacher' model. In the second stage, another recurrent policy network carefully reduces the size of each remaining layer. | * Does layer pruning.                             | https://arxiv.org/abs/1709.06030 | CMU                               | * Not good results in terms of accuracy levels. 92-93% accuracy for Cifar10                                                                                      | Dec, 2017  |
| Resource-Efficient Neural Architect                                                     | RENA uses a policy network to process the network embeddings to generate new configurations. We demonstrate RENA on image recognition and keyword spotting (KWS) problems.                                                                                                                                                                                               | * Generations of efficient DNN models. No pruning | https://arxiv.org/abs/1806.07912 | Baidu                             | * Excellent accuracy level on Cifar 10* Not clear description for method. Might not work beyond mentioned settings.* Is not published in peer-reviewed conf yet. | June, 2018 |
| SMASH: One-Shot Model Architecture Search through HyperNetworks                         | accelerate architecture selection by learning an auxiliary HyperNet that generates the weights of a main model conditioned on that model's architecture                                                                                                                                                                                                                  | * Generation of CNN Models only. No pruning       | https://arxiv.org/abs/1708.05344 | Heriot-Watt University, Edinburgh | * Hyper network for model learning* Makes search faster                                                                                                          | Aug, 2017  |
| Efficient Architecture Search by Network Transformation                                 | a new framework toward efficient architecture search by exploring the architecture space based on the current network and reusing its weights.                                                                                                                                                                                                                           | * Generations of DNN models. No pruning           | https://arxiv.org/abs/1707.04873 | London University                 |                                                                                                                                                                  | July, 2017 |
| DARTS: Differentiable Architecture Search                                               | method is based on the continuous relaxation of the architecture representation, allowing efficient search of the architecture using gradient descent.                                                                                                                                                                                                                   | * Generations of DNN models. No pruning           | https://arxiv.org/abs/1806.09055 | CMU                               | * Uses trick of using softmax action selection for making continous relaxation                                                                                   | Aug, 2017  |
| ADC: Automated Deep Compression and Acceleration with Reinforcement Learning            | leverages reinforcement learning in order to efficiently sample the design space and greatly improve the model compression quality.                                                                                                                                                                                                                                      | * Does layer pruning of already existing network  | https://arxiv.org/abs/1802.03494 | SongHan, MIT                      | * Uses continous space reinforment learning to predict the level of pruning possible                                                                             | Feb, 2018  |