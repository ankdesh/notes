## Python Environments for development

### virtualenv

```sh
* Create new project, (-p for specifying python version)
cd <project_folder>
virtualenv [-p /usr/bin/python2.7] <project_name>
```

* Activate an env
```sh
source my_project/bin/activate
```

* Deactivate the env
```sh
deactivate
```

* Freeze all requirements from current environment
```sh
pip freeze > requirements.txt
```

* Install all requirements for setting an environment
```
pip install -r requirements.txt
```

### Conda

* Create new environment using conda 
```sh 
$ conda create -n <name> python=2.7
```

* List all conda environments
```sh 
$ conda info --envs
```

* Acticate an environment 
```sh 
$ source activate <name>
```

* Remove a conda emnvironment
```sh 
$ conda remove --name <name> --all
```

* Install a package in the environment 
```sh 
$ conda install <package-name>
```

* Update a package in conda environment
```sh 
$ conda upgrade <name>
```

