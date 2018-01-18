## Setup Ubuntu 16.04 routine
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

* In case Ctrl+Alt+F1 does not give terminal, add *nomodeset* to the GRUB_CMDLINE_LINUX_DEFAULT (from https://askubuntu.com/questions/162535/why-does-switching-to-the-tty-give-me-a-blank-screen)

``` 
sudo vim /etc/default/grub
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash nomodeset"
sudo update-grub
sudo reboot
``` 

* Blacklist Nouveau
```
Add following lines to /etc/modprobe.d/blacklist-nouveau.conf (use sudo)
blacklist nouveau
blacklist lbm-nouveau
options nouveau modeset=0
alias nouveau off
alias lbm-nouveau off
```

```
sudo update-initramfs -u
```

* Install Nvidia Drivers & Cuda+Cudnn

  * Download from .deb file from https://developer.nvidia.com/cuda-80-ga2-download-archive
  * Get cudnn from https://developer.nvidia.com/compute/machine-learning/cudnn/secure/v6/prod/8.0_20170307/cudnn-8.0-linux-x64-v6.0-tgz
  * Ctrl+Alt+1
  ```
    sudo service lightdm stop
    sudo dpkg -i cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64.deb
    sudo apt-get update
    sudo apt-get install cuda
  ```
  * Extract cudnn and move files to /usr/local/cuda-8.0/lib64/ and /usr/local/cuda-8.0/include/

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
   
