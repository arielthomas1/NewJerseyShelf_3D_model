### [Draft for Readme file]

This repository includes all necessary tools to reproduce a 3D Hydrogeological model of the New Jersey shelf centered on IODP Expedition well sites M27, M28 and M29.

It accompanies a study that presents an interdisciplinary workflow incorporating borehole data, 2D depth migrated seismic profiles and prior knowledge of the depositional setting, to constrain a stochastic porosity model of the New Jersey shelf. We also perform a Petrophysical conversion to a corresponding permeability distribution. The model dimensions are 134 km x 69 km x 1.7 km. The integrated approach successfully translates small-scale porosity variations to a shelf-scale model that captures key characteristics of the New Jersey shelf wave-dominated depositional environment. The fully characterized flow model has been generated using open-source packages, GemPy and GSTools, and can be reproduced at any resolution fit to purpose with the accompanying code.


[An overview of the modeling workflow ](https://git.rwth-aachen.de/athomas/nj3d_model/-/blob/master/ModelingOverview.png)

Folder  structure?

Notebooks
* (1) Pre-processing ? (Ariel)
* (2) Geo-structural modeling (Jan)
    * Input: surface data, orientation data
    * Output: Gempy model, discretization (grid)
* (3) Variogram modeling (Jan)
    * Input: Well logs, processed seismic
    * Output: Variogram parameter table
* (4) Geostatistcal modeling (Jan)
    * Input: Geo-structural model, variogram parameter table, Well logs, 
    * Output: Single realization of porosity model
* (5) Post-processing (Ariel)
    * Input: Porosity model 
    * Output: Permeability conversion
* (6) Plotting routines
