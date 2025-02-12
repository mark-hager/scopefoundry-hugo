---
title: Analyze with ipynb
description: Given a folder with .h5 files, use this feature to analyze data quickly. It provides convenient loading functions and an overview Jupyter notebook
date: 2025-01-01
weight: 3
---

[getting_started_docs]:/docs/1_getting-started/


## Recommendation

This feature requires to have Jupyter notebook installed. It works best launch a ipynb-file (e.g. double-clicking) opens a Jupyter editor. One *recommended* way:

1. Install [Visual Studio Code](https://code.visualstudio.com/download)
2. Install extensions:
   1. Pylance (Microsoft)
   2. Jupyter (Microsoft)


## Trigger feature

There are 2 ways to start that feature. 

1. From ScopeFoundry: Advanced -> analyze with ipynb. The folder acted upon is the one defined in the `app/save_dir` settings (bottom left panel)

    ![Screenshot 2025-01-12 at 17.45.20](launch_analyze.png)

2. Using ScopeFoundry tools (install instructions [here][getting_started_docs])
	```sh
	cd "to / your_folder_with_data"
	```
	
	potentialy (`conda activate scopefoundry`)
	```sh
	python -m ScopeFoundry.tools
	```
	
	then click the corresponding button on the Welcome tap. 


## Benefit

This feature generates

1. `h5_data_loaders.py` file containing convenience methods based on the .h5 files content
2. an `overview.ipynb` where you can start your analysis

![analyze_with_ipynb](analyze_with_ipynb.png)

In the notebook the top 2 cells are generated:

In cell 1: imports of data loaders

In cell 2: lists path to each .h5 file and how it could be loaded 
