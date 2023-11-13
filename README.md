# GitHub-Rasters
Exercise for GEOG 728 Programming for Geographic Analysis at Kansas State University

### Instructions:

Accept the GitHub Classroom assignment <code>GitHub-Raster</code> and clone the new repository as a local personal repository.  The compressed ArcGIS Pro project file for this week is too large to store in GitHub and, instead, can be found in this week's Canvas module or <code>W:\GEOG\Courses\GEOG728\Exercises</code>,  Uncompress the provided ZIP file to access the ArcGIS Pro project file in your local repository workspace.  The only file which needs to be pushed to origin at the conclusion of the exercise is a single Python script.  There is no requirement to prepare and submit a script-based tool.  Should you encounter difficulties during the week, seek assistance by posting an issue in GitHub.

### Task:

Edit the provided Python file called <code>GitHub-Rasters.py</code> to create a new stand-alone script that includes the following features and capabilities.  For this script, there is no requirement to include user-defined inputs or any messaging, except for a custom print message should your script throw an exception (see the requirement below for a "try-except" block):

1. Incorporates an insert cursor to add five new observations of lesser prairie chickens to the existing feature class <code>tympanuchus_pallidicinctus</code>.  
2. Uses the Python <code>fileinput</code> module and related methods to read in the new observations in the provided text file <code>newchickens.txt</code>.
3. Incorporates an update cursor to add the species name *Tympanuchus pallidicinctus* to the "label" field, x- and y-coordinates of each observation to the "long" and "lat" fields, and a value of 1 to the "abundance" field of the new records in the final output.
4. Finishes by computing a minimum bounding polygon as a rough estimate of the species range.  For this, use the function [<code>arcpy.management.MinimumBoundingGeometry</code>](https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/minimum-bounding-geometry.htm) using the geometry type CONVEX_HULL.  Read the tool help file for this function closely, as it may have special licensing or extension requirements to account for in your script.
5. Includes at least one "try-except" block to trap geoprocessing errors.

Also include in your script a section that establishes the following three, and only these three, local variables.  Modify the path to the <code>inFile</code> variable so it works properly on your computer.

<code>inFile = "D:/GitHub/GitHub-OtherCursors/newchickens.txt"</code><br>
<code>inFc = "tympanuchus_pallidicinctus"</code><br>
<code>pt = arcpy.Point()</code>

## Rubric:

Review the assignment rubric available on Canvas for additional details on how your work will be assessed. Double-check that your script includes a complete header section, uses good commenting, incorporates line spaces between blocks of code, and reads input and writes output to current workspace.

## Submission:

Commit your code changes for <code>GitHub-Rasters.py</code> to your assignment repository on GitHub.
