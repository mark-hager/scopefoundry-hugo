---
title: New microscope app
description: Learn how to setup ScopeFoundry and create your first Microscope App
date: 2025-01-01
weight: 1
---

[IDE]:/docs/100_development/10_setup_eclipse/

[getting_started_docs]:/docs/1_getting-started/

**Required** install [ScopeFoundry](getting_started_docs)


After installation, use anaconda prompt and navigate to where you want or have the source code for your setup and start ScopeFoundry.tools:

```sh
# cd "to/your_project_folder"
conda activate scopefoundry
```

```sh
python -m ScopeFoundry.tools
```

![tools_new_app](tools_new_app.png)Go to the `new app` and press `new app`. This copied the scope foundry example files to your project folder. In your anaconda(3) prompt run:

```sh
python example_slowscan_app.py
```

you should see:

![example_microscope_app](example_microscope_app.png)

### Folder structure and take home messages

Now is a good time to learn the bare minimum of ScopeFoundry. On the left panel you see a 2 lists.  

1. Hardware: are made of `HardwareComponent` who job it is to establish a connection to your hardware, readout and set values. 

2. Measurements: are made of `Measurement` classes that define the procedures of aquiring and saving data. They can have graphical user interfaces shown on the right. Can you start the example_2d_scan?

Note that you can expand the the item in either list to expose `settings` that can be linked to the state of the hardware and parameterize you measurements respectively.

The folder structure should be of this form: 


```sh
├── your_project_folder
    ├── ScopeFoundryHW
     	├── company1_model1 
      	├── docs # optional
	     		├── links.json 	
     		├── company1_model1_hw.py					
     		├── company1_model1_dev.py			
     		├── company1_model1_test_app.py
     		├── Licence
     		├── README.md     		
     		**
     	**
    ├── fancy_app.py
    ├── your_measurement_1.py
    ├── **
    
    # after databrowser tutorial
    ├── viewers.py
    	├── images.py	
    ├── fancy_data_browser.py
    
```

In particular the folder contains:

1. A subfolder `ScopeFoundryHW` containing hardware control code. There must be at least a file, typically ending with `_hw.py`, that contains a subclass of type `HardwareComponent`.
2. measurement files containing `Measurement` subclasses.
3. The actual app file where `Measurement` und `HardwareComponent` are added to the main app. That is the file that gets run.

Congratulations, you have created your first microscope and saw the 3 most prutent high level concepts. `HardwareComponent` and `Measurement` can each have `settings`.


## Next Steps

Now that you have interacted with ScopeFoundry and built a microscope app with pre-built components, you probably would like to build a system that allows you to do real scientific experiements. To do this have a look at tutorials on how to build


1.	a custom [Hardware Component](../2_hardware-1)
2.	a custom [Measurement](../3_measurement)

or make a quick detour to setup [IDE]