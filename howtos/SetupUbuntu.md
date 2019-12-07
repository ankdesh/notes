## Setup Ubuntu 18.04 routine
### List of things-to-do after fresh Ubuntu install

* Install Google Chrome from
```
https://www.google.com/chrome/browser/desktop/index.html
```

* Gen ssh key and add to Github repo
```
ssh-keygen -t rsa
```

* Setup scripts 
```
sudo apt-get install git
git clone git@github.com:ankdesh/DevSetup.git
cd DevSetup
./scripts/setup_git.sh
./scripts/setup_rc.sh
```

* Install basic Develop stuff
``` 
sudo apt-get install -y  git   vim   gcc   g++   ipython   wget   screen 
```

* Install Nvidia Drivers & Cuda+Cudnn
```
sudo add-apt-repository ppa:graphics-drivers
sudo apt-get update
sudo ubuntu-drivers devices
sudo ubuntu-drivers autoinstall
```

* Install nvidia-docker
  * Install Docker CE
  ```
    sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    sudo apt-get update
    sudo apt-get install docker-ce
    sudo addgroup ankdesh docker
  ```
  * Install nvidia-docker
  ```
    curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
    curl -s -L https://nvidia.github.io/nvidia-docker/ubuntu16.04/amd64/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
    sudo apt-get update
    sudo apt-get install -y nvidia-docker2
    sudo pkill -SIGHUP dockerd
  ```
  * Test installations (would need a reboot after adding ankdesh to docker group to run without sudo)
  ```
    sudo docker run hello-world
    docker run --runtime=nvidia --rm nvidia/cuda nvidia-smi
  ```
   
