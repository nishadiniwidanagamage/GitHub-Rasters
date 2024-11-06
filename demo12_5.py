#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    File name: demo12_5.py
#    Author: Shawn Hutchinson
#    Description:  Calculate slope and convert DEM units to feet (if needed)
#    Date created: 11/13/2023
#    Python Version: 3.9.16

# Import required modules and classes:
import arcpy, os

# Set environment(s)
arcpy.env.workspace = "D:/GitHub/GitHub-Rasters/ExerciseData.gdb"
arcpy.env.overwriteOutput = True

# Establish local variable(s)
inRaster = "dem10"
outRaster = "slope10_5"
outWorkspace = "D:/GitHub/GitHub-Rasters/GitHub-Rasters.gdb"

# Perform geoprocessing and trap errors
try:
    if arcpy.CheckExtension("Spatial") == "Available":
        arcpy.CheckOutExtension("Spatial")
        desc = arcpy.Describe(inRaster)
        if desc.spatialReference.linearUnitName == "Meter":
            demGrid = arcpy.Raster(inRaster)
            outGrid = demGrid * 3.28084
            outSlope = arcpy.sa.Slope(outGrid)
            outSlope.save(os.path.join(outWorkspace, outRaster))
            arcpy.CheckInExtension("Spatial")
        else:
            print("Grid units = {0}, conversion not needed.".format
            (desc.spatialReference.linearUnitName))
            outGrid = arcpy.sa.Slope(inRaster)
            outGrid.save(os.path.join(outWorkspace, outRaster))
            arcpy.CheckInExtension("Spatial")
    else:
        print("Required extension not available.")
except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))
