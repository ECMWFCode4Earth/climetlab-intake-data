## intake-data

A dataset plugin for climetlab for the dataset intake-data/noaa-ersst.


Features
--------

In this README is a description of how to get the intake-data.

## Datasets description

There are two datasets: 

### 1 : `noaa_ersst`


### 2
TODO


## Using climetlab to access the data (supports grib, netcdf and zarr)

See the demo notebooks here (https://github.com/ecmwf-lab/climetlab_intake_data/notebooks

https://github.com/ecmwf-lab/climetlab_intake_data/notebooks/demo_noaa_ersst.ipynb
[nbviewer] (https://nbviewer.jupyter.org/github/climetlab_intake_data/blob/main/notebooks/demo_noaa_ersst.ipynb) 
[colab] (https://colab.research.google.com/github/climetlab_intake_data/blob/main/notebooks/demo_noaa_ersst.ipynb) 

The climetlab python package allows easy access to the data with a few lines of code such as:
```

!pip install climetlab climetlab_intake_data
import climetlab as cml
ds = cml.load_dataset(""intake-data-noaa-ersst", date='20201231',)
ds.to_xarray()
```
