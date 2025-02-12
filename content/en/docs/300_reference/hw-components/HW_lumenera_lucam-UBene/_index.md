
---
title: HW_lumenera_lucam (UBene)
description: No description available.
weight: 25
---
- [GitHub Repository](https://github.com/UBene/HW_lumenera_lucam)
- Last Updated: 2023-01-27T22:33:51Z


#### To add to your app:

`cd to/your_project_folder` and use the following cmd (requires [git](/docs/100_development/20_git/))

```bash
mkdir ScopeFoundryHW/lumenera_lucam && cd ScopeFoundryHW/lumenera_lucam && git init --initial-branch=main && git remote add upstream_UBene https://github.com/UBene/HW_lumenera_lucam && git pull upstream_UBene main && cd ../..
```

## Readme
ScopeFoundryHW.lumenera_lucam
=============================

ScopeFoundry hardware plug-in to control lucam based Lumenera cameras. Tested with Infinity 2


ScopeFoundry is a Python platform for controlling custom laboratory 
experiments and visualizing scientific data

<http://www.scopefoundry.org>

This software is not made by or endorsed by the device manufacturer

Based on low level python API by Christoph Gohlke 

Author
----------

Benedikt Ursprung 

Requirements
------------

	* ScopeFoundry
	* numpy
	* lucamapi.dll
	
	
History
--------

### 0.1.0	2023-01-27	Initial public release.

Plug-in has been used internally and has been stable.
Check Git repository for detailed history. Tested with Infinity 2

