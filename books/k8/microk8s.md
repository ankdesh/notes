### Installation
```sh
sudo snap install microk8s --classic --channel=1.21/stable
sudo usermod -a -G microk8s $USER
sudo chown -f -R $USER ~/.kube
microk8s status --wait-ready
sudo microk8s status --wait-ready
```

### Concepts
![](imgs/1.png{:height="50%" width="50%"}
![](imgs/2.png{:height="50%" width="50%"}


### Kubectl
* Setup Kubectl
```sh
echo "alias kubectl='microk8s.kubectl'" >> ~/.bashrc
```
* Get commands
```sh
kubectl get node
kubectl get severices
