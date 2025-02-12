
---
title: HW_thorlabs_powermeter (ScopeFoundry)
description: No description available.
weight: 42
---
- [GitHub Repository](https://github.com/ScopeFoundry/HW_thorlabs_powermeter)
- Last Updated: 2024-08-12T00:38:50Z


#### To add to your app:

`cd to/your_project_folder` and use the following cmd (requires [git](/docs/100_development/20_git/))

```bash
mkdir ScopeFoundryHW/thorlabs_powermeter && cd ScopeFoundryHW/thorlabs_powermeter && git init --initial-branch=master && git remote add upstream_ScopeFoundry https://github.com/ScopeFoundry/HW_thorlabs_powermeter && git pull upstream_ScopeFoundry master && cd ../..
```

## Readme
ScopeFoundryHW.thorlabs_powermeter
==================================

Thorlabs PM100D powermeter hardware plug-in for ScopeFoundry.

This interface uses the PyVISA 1.5 library to communicate over USB.

Hardware information available from Thorlabs:
<https://www.thorlabs.com/thorproduct.cfm?partnumber=PM100D>

ScopeFoundry is a Python platform for controlling custom laboratory 
experiments and visualizing scientific data

<http://www.scopefoundry.org>

This software is not made by or endorsed by Thorlabs, Inc.


Author
----------

Edward S. Barnard <esbarnard@lbl.gov>


Requirements
------------

 * ScopeFoundry
 *  [PyVisa](https://pyvisa.readthedocs.io/en/stable/)
 * [Legacy Thorlabs driver](https://www.thorlabs.com/software_pages/viewsoftwarepage.cfm?code=PM100x)

 
How to Install
---------------

pip install pyvisa
