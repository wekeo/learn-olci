# Learn OLCI

The **learn-olci** module consists of a collection of python-based Jupyter-notebooks 
design to demonstrate the capability of the Ocean and Land Colour Instrument (OLCI), 
carried by the Sentinel-3 satellites, and to help users begin to work with its data 
at level-1B and level-2. 

For any questions about this repository, please contact ops@eumetsat.int.

## License
 
This code is licensed under an MIT license. See file LICENSE.txt for details on 
the usage and distribution terms. No dependencies are distributed as part of this 
package. Copyright EUMETSAT 2022.

All product names, logos, and brands are property of their respective owners. 
All company, product and service names used in this website are for identification 
purposes only.

## Authors

* [**Ben Loveday**](mailto://ops@eumetsat.int) - [EUMETSAT](http://www.eumetsat.int)
* [**Hayley Evers-King**](mailto://ops@eumetsat.int) - [EUMETSAT](http://www.eumetsat.int)

Please see the AUTHORS.txt file for more information on contributors.

## Prerequisites

You will require `Jupyter Notebook` to run this code. We recommend that you install 
the latest [Anaconda Python distribution](https://www.anaconda.com/) for your 
operating system. Anaconda Python distributions include Jupyter Notebook.

## Dependencies

|item|version|licence|package info|
|---|---|---|---|
|python|3.8.13|PSF|https://docs.python.org/3/license.html|
|xarray|0.21.1|Apache-2.0|https://anaconda.org/conda-forge/xarray|
|netcdf4|1.5.8|MIT|https://anaconda.org/conda-forge/netcdf4|
|shapely|1.8.0|BSD-3|https://anaconda.org/conda-forge/shapely|
|matplotlib|3.5.1|PSFL|https://matplotlib.org/stable/users/project/license.html|
|cartopy|0.20.2|LGPL-3|https://scitools.org.uk/cartopy/docs/latest/copyright.html|
|notebook|6.4.8|BSD-3|https://anaconda.org/conda-forge/notebook|
|jupyter_contrib_nbextensions|0.5.1|BSD-3|https://anaconda.org/conda-forge/jupyter_contrib_nbextensions|
|ipywidgets|7.6.5|BSD-3|https://anaconda.org/conda-forge/ipywidgets|
|scikit-image|0.19.1|BSD-3|https://anaconda.org/conda-forge/scikit-image|
|plotly|5.6.0|MIT|https://anaconda.org/conda-forge/plotly|
|bokeh|2.4.2|BSD-3|https://anaconda.org/conda-forge/bokeh|
|hda|0.2.2|Apache-2.0|https://pypi.org/project/hda/|
|eumartools|0.0.1|MIT|https://anaconda.org/cmts/eumartools|
|ipykernel|6.4.1|BSD-3|https://anaconda.org/conda-forge/ipykernel|
|cmocean|2.0|MIT|https://anaconda.org/conda-forge/cmocean|
|eumdac|1.0.0|MIT|https://anaconda.org/eumetsat/eumdac|

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

`git clone --recurse-submodules --remote-submodules https://gitlab.eumetsat.int/eumetlab/oceans/ocean-training/sensors/learn-olci.git`

This will make a local copy of all the relevant files.

*Note: If you find that you are missing packages, you should check that you ran 
`git clone` with both the `--recurse-submodules` and `--remote-submodules` options.*

*Note: if you are using an older version of git, you may find that your submodules are empty. In this case, you need to remove the folder and re-run the line above with `--recursive` added to the end*

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

This module is based around a series of [Jupyter Notebooks](https://jupyter.org/). These support high-level interactive learning by allowing us to combine code, text description and data visualisations. If you have not worked with `Jupyter Notebooks` 
before, please look at the [Introduction to Python and Project Jupyter](./working-with-python/Intro_to_Python_and_Jupyter.ipynb) module to get a short introduction to their usage and benefits.

To to run Jupyter Notebook, open a terminal or Anaconda prompt and make sure you have activated 
the correct environment. Again, navigate to the repository folder.

If you are running this code for the first time in this environment, you need to enable two
`extensions` to Jupyter by running the following commands.

`jupyter nbextension enable --py widgetsnbextension` \
`jupyter nbextension enable exercise2/main`

*Note: you can also enable these in the **Nbextensions** tab of the Jupyter browser window* 

Now you can run Jupyter using:

`jupyter notebook` or `jupyter-notebook`, depending on your operating system.

This should open Jupyter Notebooks in a browser window. On occasion, Jupyter may not
be able to open a window and will give you a URL to past in your browser. Please do
so, if required.

*Note: Jupyter Notebook is not able to find modules that are 'above' it in a directory 
tree, and you will unable to navigate to these. So make sure you run the line above 
from the correct directory!*

Now you can run the notebooks! We recommend you start with the [Index](./Index.ipynb) module.

### Collaborating, contributing and issues

If you would like to collaborate on a part of this code base or contribute to it 
please contact us on copernicus.training@eumetsat.int. If you are have issues and 
need help, or you have found something that doesn't work, then please contact us 
at ops@eumetsat.int. We welcome your feedback!

<hr>
<hr>

### Overview for advanced users

**Installation:**

`git clone --recurse-submodules --remote-submodules https://gitlab.eumetsat.int/eumetlab/oceans/ocean-training/sensors/learn-olci.git`

**Create and set environment**

`conda env create -f environment.yml` \
`conda activate cmts_learn_olci`

**WEkEO SPECIFIC**

`ipython kernel install --user --name=cmts_learn_olci`

**Activate extensions (1st run in environment, only)**

`jupyter nbextension enable --py widgetsnbextension` \
`jupyter nbextension enable exercise2/main`

**Run**

`jupyter notebook` or `jupyter-notebook`
