#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    File name: demo12_3.py
#    Author: Shawn Hutchinson
#    Description:  Extract and print even more properties of a raster
#    Date created: 11/13/2023
#    Python Version: 3.9.16

# Import required modules and classes:
import arcpy

# Set environment(s)
arcpy.env.workspace = "D:/GitHub/GitHub-Rasters/ExerciseData.gdb"

# Establish local variable(s)
raster = "LANDSAT8_20150609/Band_4"

# Describe the raster
desc = arcpy.Describe(raster)

# Print key properties of the raster dataset with the format function
print("Band Properties: \nCell Height: {0} \nCell Width: {1} \nPixel Type: {2} \nNoData Value:  {3}".format(desc.meanCellHeight, desc.meanCellWidth, desc.pixelType, desc.noDataValue))