#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    File name: demo12_2.py
#    Author: Shawn Hutchinson
#    Description:  Extract and print more properties of a raster
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
print("Format:  {0}".format(desc.format))
print("Band Count:  {0}".format(desc.bandCount))
print("Sensor:  {0}".format(desc.sensorType))
print("Compression Type:  {0}".format(desc.compressionType))
print("Permanent:  {0}".format(desc.permanent))