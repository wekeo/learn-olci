# Learn OLCI

[![Generic badge](https://img.shields.io/badge/Launch-TrainHub-Blue.svg)](https://trainhub.eumetsat.int/ocean/sensors)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gl/eumetlab%2Focean%2Fsensors%2Flearn-olci/main)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](http://colab.research.google.com/github/eumetlab/ocean/sensors/learn-olci/blob/main)
[![Open in Planetary Computer](https://img.shields.io/badge/Open-Planetary%20Computer-black?style=flat&logo=microsoft)](https://pccompute.westeurope.cloudapp.azure.com/compute/hub/user-redirect/git-pull?repo=https://github.com/eumetlab/ocean/sensors/learn-olci&branch=main)

**learn-olci** is a repository of Jupyter-Notebook based learning material that
focusses on the specifics of the Sentinel-3 OLCI sensor, its Level-1B and Level-2
products and how to use them. The notebooks are suitable for beginners to ocean
colour remote sensing, as well as intermediate level users that have experience
in ocean colour or of other remote sensing approaches. Some knowledge of Python 
is required to use this material. For any questions about this repository, please
contact ops@eumetsat.int. 

This repository can be launched in TrainHub WEkEO, Binder, colab

## License
 
This code is licensed under an MIT license. See file LICENCE.txt for details on 
the usage and distribution terms. No dependencies are distributed as part of this 
package.

All product names, logos, and brands are property of their respective owners. 
All company, product and service names used in this website are for identification 
purposes only.

## Authors

* [**Ben Loveday**](mailto://ops@eumetsat.int) - [EUMETSAT](http://www.eumetsat.int)
* [**Hayley Evers-King**](mailto://ops@eumetsat.int) - [EUMETSAT](http://www.eumetsat.int)

Please see the AUTHORS.txt file for more information on contributors.

## Prerequisites

You will require `Jupyter Notebook` to run this code. We recommend that you install 
the latest [Anaconda Python distribution]((https://www.anaconda.com/) for your 
operating system. Anaconda Python distributions include Jupyter Notebook.

## Dependencies
|item|version|licence|package info|
|---|---|---|---|
|xarray|0.21.1|Apache-2.0|https://anaconda.org/conda-forge/xarray|
|netcdf4|1.5.8|MIT|https://anaconda.org/conda-forge/netcdf4|
|shapely|1.8.0|BSD-3|https://anaconda.org/conda-forge/shapely|
|matplotlib|3.5.1|PSFL|https://matplotlib.org/stable/users/project/license.html|
|cartopy|0.20.2|LGPL-3|https://anaconda.org/conda-forge/cartopy|
|notebook|6.4.8|BSD-3|https://anaconda.org/conda-forge/notebook|
|jupyter_contrib_nbextensions|0.5.1|BSD-3|https://anaconda.org/conda-forge/jupyter_contrib_nbextensions|
|ipywidgets|7.6.5|BSD-3|https://anaconda.org/conda-forge/ipywidgets|
|scikit-image|0.19.1|BSD-3|https://anaconda.org/conda-forge/scikit-image|
|plotly|5.6.0|MIT|https://anaconda.org/conda-forge/plotly|
|bokeh|2.4.2|BSD-3|https://anaconda.org/conda-forge/bokeh|
|hda|0.2.2|Apache-2.0|https://pypi.org/project/hda/|
|eumartools|0.0.1|MIT|https://anaconda.org/cmts/eumartools|
|eumdac|1.0.0|MIT|https://pypi.org/project/eumdac/|
  
## Installation

The simplest and best way to install these packages is via Git. Users can clone this 
repository by running the following commands from either their [terminal](https://tinyurl.com/2s44595a) 
(on Linux/OSx), or from the [Anaconda prompt](https://docs.anaconda.com/anaconda/user-guide/getting-started/). 

You can usually find your terminal in the start menu of most Linux distributions 
and in the Applications/Utilities folder  on OSx. Alternatively, you should be 
able to find/open your Anaconda prompt from your start menu (or dock, or via running 
the Anaconda Navigator). Once you have opened a terminal/prompt, you should navigate 
to the directory where you want to put the code. Once you are in the correct directory, 
you should run the following command;

`git clone --recurse-submodules --remote-submodules https://gitlab.eumetsat.int/eumetlab/ocean/sensors/learn-olci`

This will make a local copy of all the relevant files.

*Note: If you find that you are missing packages, you should check that you ran 
`git clone` with both the `--recurse-submodules` and `--remote-submodules` options.*

## Usage

This collection supports Python 3.8. Although many options are possible, the 
authors highly recommend that users install the appropriate Anaconda package 
for their operating system. In order to ensure that you have all the required 
dependencies, we recommend that you build a suitable Python environment, as 
discussed below.

### Python environments

Python allows users to create specific environments that suit their applications. 
This tutorials included in this collection require a number of non-standard 
packages - e.g. those that are not included by default in Anaconda. In this 
directory, users will find a *environment.yaml* file which can be used to 
construct an environment that will install all the required packages.

To construct the environment, you should open either **terminal** (Linux/OSx) 
or an **Anaconda prompt** window and navigate to repository folder you downloaded 
in the **Installation** section above. In this folder there is a file called 
**environment.yml**. This contains all the information we need to install the relevant 
packages.

To create the environment, run:

`conda env create -f environment.yml`

This will create a Python 3.8 environment called **cmts_learn_olci**. The environment 
won't be activated by default. To activate it, run:

`conda activate cmts_learn_olci`

Now you are ready to go!

*Note: remember that you may need to reactivate the environment in every 
new window instance*

### Running Jupyter Notebook

These modules are based on [Jupyter notebooks](https://jupyter.org/). Jupyter allows 
a high-level of interactive learning, as it brings code, text description and 
visualisations into one place. If you have not worked with `Jupyter Notebooks` 
before, we recommend you start with the [Introduction to Python and Project Jupyter](./working-with-python/Intro_to_Python_and_Jupyter.ipynb) module to get a short introduction to 
their usage and benefits.

To to run Jupyter Notebook, open a terminal or Anaconda prompt and make sure you have activated 
the correct environment. Again, navigate to the repository folder.

If you are running this code for the first time in this environment, you need to enable two
`extensions` to Jupyter by running the following commands.

`jupyter nbextension enable --py widgetsnbextension` \
`jupyter nbextension enable exercise2/main`

*Note: you can also enable these in the **Nbextensions** tab of the Jupyter browser window* 

Now you can run Jupyter using:

`jupyter notebook`

This should open Jupyter Notebooks in a browser window. On occasion, Jupyter may not
be able to open a window and will give you a URL to past in your browser. Please do
so, if required.

*Note: Jupyter Notebook is not able to find modules that are 'above' it in a directory 
tree, and you will unable to navigate to these. So make sure you run the line above 
from the correct directory!*

Now you can run the notebooks!

### Collaborating, contributing and issues

If you would like to collaborate on a part of this code base or contribute to it 
please contact us on copernicus.training@eumetsat.int. If you are have issues and 
need help, or you have found something that doesn't work, then please contact us 
at ops@eumetsat.int.

<hr>
<hr>

### TL;DR for advanced users

**Installation:**

`git clone --recurse-submodules --remote-submodules https://gitlab.eumetsat.int/eumetlab/ocean/sensors/learn-olci`

**Create and set environment**

`conda env create -f environment.yml` \
`conda activate cmts_learn_olci`

**Activate extensions (1st run in environment, only)**

`jupyter nbextension enable --py widgetsnbextension` \
`jupyter nbextension enable exercise2/main`

**Run**

`jupyter notebook` or `jupyter-notebook`