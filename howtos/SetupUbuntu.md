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
