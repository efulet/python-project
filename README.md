# Welcome to Skeleton Project Directory

This defines a basic structure of your skeleton directory. This work is based 
on http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/


## Requirements

* Python (https://www.python.org/)

* setuptools (http://pypi.python.org/pypi/setuptools)
```bash
    $> wget https://bootstrap.pypa.io/ez_setup.py -O - | sudo python
```

* pip (https://pip.pypa.io/en/latest/installing.html)
```bash
    $> sudo easy_install pip
```

* virtualenvwrapper (http://virtualenvwrapper.readthedocs.org/)
```bash
    $> sudo pip install virtualenvwrapper
```


## Configure

virtualenv tool has become the de-facto standard mechanism for isolating Python 
environments. Install virtualenvwrapper for starting a new project. Run:
```bash
    $> mkvirtualenv project
```

Install requirements for this project:

* Sphinx (http://sphinx-doc.org/index.html)
```bash
    $> pip install Sphinx
```

* Coverage.py (http://nedbatchelder.com/code/coverage/)
```bash
    $> pip install pytest-cov
```

* SQLAlchemy (http://www.sqlalchemy.org/)
```bash
    $> pip install SQLAlchemy
```

Update requirements.txt. The following command list of all of the requirements 
for your project, which can later be used by the setup.py file to list your 
dependencies.


```bash
    $> pip freeze > requirements.txt
```


## Run

Print program options:
```bash
    $> bin/project.sh -h
    usage: python main.py
    
    optional arguments:
      -h, --help  show this help message and exit
      -v          verbose
```
