## Setup Ubuntu 16.04 for my preferance 
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
execute 
```
sudo update-initramfs -u
```

