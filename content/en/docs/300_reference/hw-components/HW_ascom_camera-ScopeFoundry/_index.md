
---
title: HW_ascom_camera (ScopeFoundry)
description: No description available.
weight: 6
---
- [GitHub Repository](https://github.com/ScopeFoundry/HW_ascom_camera)
- Last Updated: 2024-08-12T01:05:28Z


#### To add to your app:

`cd to/your_project_folder` and use the following cmd (requires [git](/docs/100_development/20_git/))

```bash
mkdir ScopeFoundryHW/ascom_camera && cd ScopeFoundryHW/ascom_camera && git init --initial-branch=master && git remote add upstream_ScopeFoundry https://github.com/ScopeFoundry/HW_ascom_camera && git pull upstream_ScopeFoundry master && cd ../..
```

## Readme
ScopeFoundryHW.ascom_camera
===========================

ScopeFoundry hardware plug-in for ASCOM-connected cameras.

This interface uses commuicates via ASCOM to many scientific and
astronomy camera systems.

Windows-only due to ASCOM use of the Microsoft COM interface. 

(Tested with a QSI-600 camera)


ScopeFoundry is a Python platform for controlling custom laboratory 
experiments and visualizing scientific data

<http://www.scopefoundry.org>

This software is not made by or endorsed by the ASCOM Initiative.


Author
----------

Edward S. Barnard <esbarnard@lbl.gov>


License
----------


Keywords
----------
Camera, CCD

Requirements
------------

	* [ScopeFoundry](http://www.scopefoundry.org)
	* [pywin32](https://sourceforge.net/projects/pywin32/)
	* [ASCOM](http://www.ascom-standards.org)
	* Windows XP or later

