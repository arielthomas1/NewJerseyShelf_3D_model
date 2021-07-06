### [Draft for Readme file]

Short description of project? Abstract?

Add overview image of file structure (Ariel PPT)

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
