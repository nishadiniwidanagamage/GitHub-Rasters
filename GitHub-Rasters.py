#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: GitHub-Rasters.py
    Author: Nishadini Widanagamage
    Description:  Calculate NDVI using a LANDSAT 8 image
    Date created: 11/06/2024
    Python Version: 3.9.16
"""

# Import arcpy module and allow overwriting
import arcpy
import os
from arcpy.sa import Minus, Plus, Divide

# Set workspace and allow overwrite output
arcpy.env.workspace = r"C:\Users\nishadini\OneDrive - Kansas State University\Documents\GitHub\rasters-nishadiniwidanagamage-main\ExerciseData.gdb"
arcpy.env.overwriteOutput = True

# Establish local variables 
in_raster_r = "LANDSAT8_20160510/Band_4" # Red band for Landsat 8
in_raster_nir = "LANDSAT8_20160510/Band_5" # NIR band for Landsat 8
out_workspace = r"C:\Users\nishadini\OneDrive - Kansas State University\Documents\GitHub\rasters-nishadiniwidanagamage-main\scratch.gdb"


# Error trapping using try-except 
try:
    # Checking the availability of required extensions
    if arcpy.CheckExtension("Spatial") == "Available":
        # Checking out required extensions 
        arcpy.CheckOutExtension("Spatial")

        # Rescale bands since unrescaled bands were giving NDVI range -1 to 0.
        red_band = Divide(arcpy.Raster(in_raster_r), 10000)
        nir_band = Divide(arcpy.Raster(in_raster_nir), 10000)

        # Calculate NDVI
        ndvi = Divide(Minus(nir_band, red_band), Plus(nir_band, red_band))

        # Define the output path for the NDVI raster
        output_path = os.path.join(out_workspace, "NDVI")
        
        # Save NDVI output
        ndvi.save(output_path) 
        print("NDVI calculated and saved")

        # Describe the output raster
        desc = arcpy.Describe(output_path)
        spatial_res = f"{desc.meanCellWidth} x {desc.meanCellHeight}"
        spatial_units = desc.spatialReference.linearUnitName

        # Print sucess message
        print(f"Script succeeded! Ouput saved as: {output_path}")
        print(f"Spatial resolution: {spatial_res} {spatial_units}")

        # Checking in used extensions 
        arcpy.CheckInExtension("Spatial")

    else:
        print("Spatial extension is not available")
    
except arcpy.ExecuteError:
    print("Gelprocessing error occured:")
    print(arcpy.GetMessages(2))

