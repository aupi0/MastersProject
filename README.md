# MastersProject
Masters Project Codebase
Masters Project Codebase
Creation of Symbolic Regression implementation, using Genetic Programming, to create blood glucose prediction models for type 1 diabetics.
Involves all pre-processing scripts used within this project.

Requires the NumPy (https://numpy.org/) and Pandas (https://pandas.pydata.org/) libraries within Python.

Pre-Processing of data was achieved by manually dropping unnecessary columns and any rows whose time didn't overlap between glucose and pump data, glucose data files were also combined into a singuler file.
After this reformatInsulinCarbData and reformatGlucoseData were run for each of the patient files used within this project.
All getVariable scripts rely on files created within reformatedInsulinCarbData and reformatGlucoseData, these scripts create different variables files, ready for use within the craeted symnbolicRegression program.

TimeInRange is a seperate script created to evaluate the glucose value ranges.
