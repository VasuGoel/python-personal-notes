# Python

Python programs and personal notes taken on the grind to learn Python.

## Getting Started

Start by either downloading the zip file or clone with HTTPS.

### Prerequisites

* Python 3.7.3 (https://www.python.org/downloads/) installed on your mac or windows
* Terminal (on Mac) or an IDE like PyCharm, Spyder, Jupyter notebook


## Running

### Steps to run Python programs via terminal (on Mac)

#### 1. Set $PATH for newer version of Python 3.7.x that you just installed over the pre-installed 2.x that Mac comes shipped with already.

* Open the terminal, and type 
```
nano .bash_profile
```

* Paste the following script in the Nano modeless editor
```
# Setting PATH for Python 3.7
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.7/bin:${PATH}"
export PATH

alias python=python3
alias pip=pip3
```

* Quit the terminal, and reopen it to check if newer $PATH setup for python worked by simply running the python shell.
```
python
```

* If you see something like this, then you're good to go!
```
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

#### 2. Using python to run the scripts/programs in the cloned repository

* Unzip the repository downloaded from https://github.com/VasuGoel/python

* Open terminal, change your directory to point to coursera-py4e folder. Assuming the repository downloaded in your Downloads folder.
```
cd ~/Downloads/python
```
* Pick a specific week and cd into it, like
```
cd 5.\ Strings/
```

* Run any program in that particular week, using the python command
```
python formatted_strings.py
```

## Built With

* [Python] (https://www.python.org/) - Python is an interpreted, high-level, general-purpose programming language.

## Authors

* **Vasu Goel** (https://github.com/VasuGoel)

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/VasuGoel/python/blob/master/LICENSE) file for details
