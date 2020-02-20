## Introduction to Bioinformatics

This repository contains the material created or adapted from other (referred) sources for a first introduction to Bioinformatics using Python, R and jupyter notebooks for the 2nd course in the Degree on Biomedical Sciencesat the Universitat Internacional de Catalunya.

Jordi Villà-Freixa, 2019-2020

## Getting Started

These instructions will lead you to the details needed to run the different tools ion your computer.

### Prerequisites

In order to follow the course you are encouraged to install, in this order:
* [miniconda](https://docs.conda.io/en/latest/miniconda.html)

Then, from the terminal (in Mac OS and linux) or from the Anaconda prompt (in windows):
* [jupyter notebooks](https://jupyter.org/install):
  ```
  conda install jupyter
  ```
* required initial Python packages:
  ```
  conda install biopython
  ```
* if you want to clone this repository in your computer (not needed, as you can download individual files and open them in jupyter notebook), you can install [GitHub Desktop](https://desktop.github.com) to make it the easy way.

### Tips

Typically, `jupyter notebooks`are run from the terminal (or the anaconda prompt in windows). If you use Mac you can create an `automator`application with this simple code:
```
variable="'$1'"
the_script='tell application "terminal" to do script "nbopen '
osascript -e "${the_script}${variable}\""
```
ensuring you use `bash` as the interpreter and you mark the "pass as arguments" option.

## Authors

* **Jordi Villà-Freixa** - *Initial work* - [JordiVillaFreixa](https://github.com/JordiVillaFreixa)

See also the list of [contributors](https://github.com/JordiVillaFreixa/IntroBioinfo/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
