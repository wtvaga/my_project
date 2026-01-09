# My_Package

My_Package is intended as a demonstration of packaging Python projects for distribution.

## Installation

One can install the package via **PyPI** or from **source**.

### Install from PyPI

```batch/bash
> pip install my_package
```

### Install from Source (GitHub)

```Git bash
$ git clone https://github.com/author_nickname/my_project.git
```

```batch/bash
> cd my_project

my_project> py -3.9 -m venv py3_9venv

my_project> py3_9venv\Scripts\activate

(py3_9venv) my_project> pip install .
```

## Usage

After installation, one can import `my_module` and test both the class `My_Class` and the function `my_function`.

### Example: Tests of the class and the function

```batch/bash
(py3_9venv) my_project> pytest tests -v
```

```batch/bash
(py3_9venv) my_project> python
Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from my_package import my_module
>>> import numpy as np
>>> # Test of the class My_Class
>>> arg1 = 1
>>> arg2 = 2
>>> my_obj = my_module.My_Class(arg1, arg2)
>>> result = my_obj.calculate_sum()
>>> my_obj.display()
arg1: 1.0
arg2: 2.0
arg1 + arg2 = 3.0
>>> result == np.float16(3)
np.True_
>>> # Test of the function my_function
>>> input_variable = "Test of 'Hello world!'"
>>> result = my_module.my_function(input_variable)
Test of 'Hello world!'
>>> result == "Test of 'Hello world!'"
True
>>> exit()

(py3_9venv) my_project> deactivate
```

## Process Description for Developers

Developers can the next steps follow to build, install and push the project on GitHub.

### Local Installation and Built

```batch/bash
> cd my_project

my_project> py -3.9 -m venv py3_9venv

my_project> py3_9venv\Scripts\activate

(py3_9venv) my_project> py -m pip install --upgrade pip

(py3_9venv) my_project> py -m pip install --upgrade build

(py3_9venv) my_project> py -m pip install pytest # if not in the dependencies of file .toml

(py3_9venv) my_project> pip install .
```

### Tests

```batch/bash
(py3_9venv) my_project> pytest tests -v

(py3_9venv) my_project> python
Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from my_package import my_module
>>> import numpy as np
>>> # Test of the class My_Class
>>> arg1 = 1
>>> arg2 = 2
>>> my_obj = my_module.My_Class(arg1, arg2)
>>> result = my_obj.calculate_sum()
>>> my_obj.display()
arg1: 1.0
arg2: 2.0
arg1 + arg2 = 3.0
>>> result == np.float16(3)
np.True_
>>> # Test of the function my_function
>>> input_variable = "Test of 'Hello world!'"
>>> result = my_module.my_function(input_variable)
Test of 'Hello world!'
>>> result == "Test of 'Hello world!'"
True
>>> exit()

(py3_9venv) my_project> deactivate
```

### Removal of unneccessary Files and Push on GitHub

```batch/bash
my_project> rmdir /S py3_9venv

my_project> rmdir /S .pytest_cache

my_project> rmdir /S my_package\__pycache__

my_project> rmdir /S tests\__pycache__

my_project> cd ..

> mkdir GitHub

> cp my_project GitHub

> exit
```

Open the browser:
- go to: [https://www.github.com](https://www.github.com)
- login with author credentials (author nickname and password)
- create a new repository called `my_project`

```Git bash
$ cd /d/GitHub

$ git init

$ git add .

$ git commit -m "Initial commit"

$ git remote add origin https://github.com/author_nickname/my_project.git

$ git branch - M main

$ git push -u origin main

$ exit
```

