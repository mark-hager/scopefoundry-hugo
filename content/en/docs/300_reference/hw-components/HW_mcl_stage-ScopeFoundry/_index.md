
---
title: HW_mcl_stage (ScopeFoundry)
description: MadCityLabs Nanopositioner Stage ScopeFoundry Hardware component
weight: 26
---
- [GitHub Repository](https://github.com/ScopeFoundry/HW_mcl_stage)
- Last Updated: 2020-12-21T20:34:38Z


#### To add to your app:

`cd to/your_project_folder` and use the following cmd (requires [git](/docs/100_development/20_git/))

```bash
mkdir ScopeFoundryHW/mcl_stage && cd ScopeFoundryHW/mcl_stage && git init --initial-branch=master && git remote add upstream_ScopeFoundry https://github.com/ScopeFoundry/HW_mcl_stage && git pull upstream_ScopeFoundry master && cd ../..
```

## Readme
ScopeFoundryHW.mcl_stage
=====================

MadCityLabs Piezo USB plug-in for ScopeFoundry.

This interface uses the MadLib device driver from MadCityLabs to
control MadCityLabs stages controlled by Nano-Drive piezo controllers.
To use this, please contact MadCityLabs for the required software and DLL. 

It has been tested with 2 and 3 axis NanoPDQ stages.

ScopeFoundry is a Python platform for controlling custom laboratory 
experiments and visualizing scientific data

<http://www.scopefoundry.org>

This software is not made by or endorsed by MadCityLabs, Inc.


Authors
----------

Edward S. Barnard <esbarnard@lbl.gov>


Requirements
------------

	* ScopeFoundry

