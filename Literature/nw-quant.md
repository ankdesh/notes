## Literature survey for Neural network Quantization 


| Title                                                                                   | Summary                                                                                                                                                                                                                                                                                                                                                                  | Link                             | Affiliations      |
|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|-------------------|
|Deep Learning with Limited Numerical precision   | [Summary](#Deep-Learning-with-Limited-Numerical-precision) | https://arxiv.org/abs/1502.02551 | Gupta et.al. IBM              |
|Trained Ternary Quantization   | [Summary](#Trained-Ternary-Quantization) | https://arxiv.org/abs/1612.01064 | Zhu et.al. Stanford              |
| Model Compression via Distillation and Quantization   | [Summary](#Deep-Learning-with-Limited-Numerical-precision) | https://arxiv.org/abs/1802.05668 | Polino et.al. DeeoMind, ETH Zuirch              |

### Deep Learning with Limited Numerical precision (Gupta et.al)
* Uses rounding modes 
  * Round-to-nearest.
  * Stochastic rounding.
  
![](images/gupta-et-al.png)

### Trained Ternary Quantization (Zhu et. al)
* Learn both the ternary weights and scale factors per layer. Both, positivie and negative scale factors are learned.
![](images/zhu-et-al.png)

### Model Compression via Distillation and Quantization (Polino et. al.) 
* Two different methods. 
  1. *Quantized distillation*, aims to leverage distillation loss during the training process, by incorporating it into the training of a student network whose weights are constrained to a limited set of levels. 
  2. *Differentiable quantization*, attempts to converge to the optimal location of quantization points through stochastic gradient descent.

* Quantized Distillation

![](images/polini-et-al.png)

* Differentiable quantization

![](images/polinio-differentiable-quant.png)

* Future works suggestes use of reinforcement learning. 
  * While the loss is continuous w.r.t. p, there are indirect effects when changing the way each weight
gets quantized. This can have drastic effect on the learning process. To avoid such issues, we rely on the following set of heuristics. Future work will look at adding a reinforcement learning loss for how the pi are assigned to weights.
