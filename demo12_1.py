#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    File name: demo12_1.py
#    Author: Shawn Hutchinson
#    Description:  Extract and print properties of a raster
#    Date created: 11/13/2023
#    Python Version: 3.9.16

# Import required modules and classes:
import arcpy

# Set environment(s)
arcpy.env.workspace = "D:/GitHub/GitHub-Rasters/ExerciseData.gdb"

# Establish local variable(s)
raster = "LANDSAT8_20150609"

# Describe the raster
desc = arcpy.Describe(raster)

# Print key properties of the raster dataset with the format function
print("Raster Properties: \nDataset type: {0} \nSpatial Reference: {1} \nUnits: {2} \nExtent:{3}".format(desc.datasetType, desc.spatialReference.name, desc.spatialReference.linearUnitName, desc.extent))