
---
title: HW_acton_spec (UBene)
description: Acton Spectrometer 2300i ScopeFoundry Hardware Component
weight: 48
---
- [GitHub Repository](https://github.com/UBene/HW_acton_spec)
- Last Updated: 2022-03-30T13:44:52Z
- Forked from [HW_acton_spec (ScopeFoundry)](/docs/300_reference/hw-components/hw_acton_spec-scopefoundry)

#### To add to your app:

`cd to/your_project_folder` and use the following cmd (requires [git](/docs/100_development/20_git/))

```bash
mkdir ScopeFoundryHW/acton_spec && cd ScopeFoundryHW/acton_spec && git init --initial-branch=master && git remote add upstream_UBene https://github.com/UBene/HW_acton_spec && git pull upstream_UBene master && cd ../..
```

## Readme
ScopeFoundryHW.acton_spec
=====================

Princeton Instruments / Acton 2300i Spectrometer plug-in for ScopeFoundry.

This interface uses the RS-232 or USB-serial interface to Acton spectrometers

It has been tested with Acton 2300i and 300 series spectrometers


ScopeFoundry is a Python platform for controlling custom laboratory 
experiments and visualizing scientific data

<http://www.scopefoundry.org>

This software is not made by or endorsed by Princeton Instruments, Inc.


Authors
----------

Edward S. Barnard <esbarnard@lbl.gov>


Requirements
------------

	* ScopeFoundry
	* PySerial

