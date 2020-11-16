```python
import torch
from torch import nn
```

## Generate Data


```python
N = 1000000 # Number of samples
```

Here we take two gaussian models with mean 2.0 and 5.0 respectively (and variance 1.0).


```python
gauss_orig0 = torch.distributions.Normal(torch.tensor([2.0]), torch.tensor([1.0]))
gauss_orig1 = torch.distributions.Normal(torch.tensor([5.0]), torch.tensor([1.0]))
```

Now we generate samples from two distributions and also two vectors of data centered at 2.0 and 5.0


```python
x0 = gauss_orig0.sample((N,))
x1 = gauss_orig1.sample((N,))
x0_meanSamples = torch.ones((N,)) * 2.0 # All values centered at mean of Gauss 0
x1_meanSamples = torch.ones((N,)) * 5.0 # All values centered at mean of Gauss 0
```


```python
print (x0.size())
print (x0.mean())
print (x0_meanSamples.size(), x0_meanSamples[:5])
```

    torch.Size([1000000, 1])
    tensor(1.9999)
    torch.Size([1000000]) tensor([2., 2., 2., 2., 2.])


Now we calculate the likelihood of the two models with different samples. We expect the likelihood to be high when samples agree to the model. 
### Note to Future self: If this is unclear, read your notes in Evernote


```python
print ('Likelihood prob -> model = gauss0, data ~ gauss0 :::',torch.exp(gauss_orig0.log_prob(x0).mean())) # 
print ('Likelihood prob -> model = gauss0, data ~ gauss1 :::',torch.exp(gauss_orig0.log_prob(x1).mean())) # 
print ('Likelihood prob -> model = gauss1, data ~ gauss0 :::',torch.exp(gauss_orig1.log_prob(x0).mean())) # 
print ('Likelihood prob -> model = gauss1, data ~ gauss1 ::: ',torch.exp(gauss_orig1.log_prob(x1).mean())) # 

print ('Likelihood prob -> model = gauss0, data = 2.0 :::',torch.exp(gauss_orig0.log_prob(x0_meanSamples).mean())) # 
print ('Likelihood prob -> model = gauss0, data = 5.0 :::', torch.exp(gauss_orig0.log_prob(x1_meanSamples).mean())) # 
```

    Likelihood prob -> model = gauss0, data ~ gauss0 ::: tensor(0.2422)
    Likelihood prob -> model = gauss0, data ~ gauss1 ::: tensor(0.0027)
    Likelihood prob -> model = gauss1, data ~ gauss0 ::: tensor(0.0027)
    Likelihood prob -> model = gauss1, data ~ gauss1 :::  tensor(0.2421)
    Likelihood prob -> model = gauss0, data = 2.0 ::: tensor(0.3989)
    Likelihood prob -> model = gauss0, data = 5.0 ::: tensor(0.0044)



```python

```
