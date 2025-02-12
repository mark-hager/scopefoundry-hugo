---
title: Getting Started
description: Installing ScopeFoundry and its dependencies.
weight: 1
---

[anaconda_dl]:https://www.anaconda.com/download/success
[ anaconda_env_docs ]: http://conda.pydata.org/docs/using/envs.html
[IDE]:/docs/100_development/10_setup_eclipse/

**We recommend** the [Anaconda][anaconda_dl] Python distribution, which contains many easy-to-install scientific python packages and recommend to create a separate environment. 

If you already had a non-Anaconda version of python installed, you will need to make sure you use Anaconda in order to follow the instructions below. The use of the conda environment is optional, but provides a clean, known working environment for ScopeFoundry.

###### Windows

1. Download and install [mininaconda](anaconda_dl) Python distribution 
2. Create an environment with the required dependencies. Anaconda provides a way to make a clean set of packages in an [environment][anaconda_env_docs]. To create an environment called "scopefoundry" use `anaconda(3) prompt` to run:
	```sh
	conda create -n scopefoundry python=3.13
	```
	To include ScopeFoundry and all of the packages ScopeFoundry needs to run activate the environment:
	```sh
	conda activate scopefoundry
	```
3. To download and install ScopeFoundry and it's dependencies
	```sh
	pip install pyqt6 qtconsole matplotlib scopefoundry
	```

	*where `qtconsole`, `matplotlib` are optional*

###### Mac / Linux

Same step as above for Windows except that 

- you can use `terminal` instead of `anaconda prompt`.

- for older versions of anaconda (<4.4 before 2017) you have to replace `conda activate scopefoundry` with 
	```sh
	source activate scopefoundry
	```

### Next

- check your installation by [making your first app](/docs/11_tools-tutorials/1_new-microscope-app/) in 2 min

- setup recommended [editor (IDE)][IDE] for easier code manipulation

