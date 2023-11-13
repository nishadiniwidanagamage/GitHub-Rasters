# GitHub-Rasters
Exercise for GEOG 728 Programming for Geographic Analysis at Kansas State University

### Instructions:

Accept the GitHub Classroom assignment <code>GitHub-Raster</code> and clone the new repository as a local personal repository.  The compressed ArcGIS Pro project file for this week is too large to store in GitHub and, instead, can be found in this week's Canvas module or <code>W:\GEOG\Courses\GEOG728\Exercises</code>,  Uncompress the provided ZIP file to access the ArcGIS Pro project file in your local repository workspace.  The only file which needs to be pushed to origin at the conclusion of the exercise is a single Python script.  There is no requirement to prepare and submit a script-based tool.  Should you encounter difficulties during the week, seek assistance by posting an issue in GitHub.

### Task:

Edit the provided Python file called <code>GitHub-Rasters.py</code> to create a new stand-alone script that calculats normalized difference vegetation index (NDVI) from a multi-band raster dataset.  Be sure your script includes the following features and capabilities.  For this script, there is no requirement to include user-defined inputs or any messaging, except for a custom print message should your script throw an exception (see the requirement below for a "try-except" block):

1. Uses one of the three available Landsat 8 images as the raster input.
2. Uses at least one, but no more than three, local variables.
3. Uses only Spatial Analyst functions – no Python math!
4. Checks out/in the Spatial Analyst extension.
5. Uses at least one "if-else" and "try-except" block for error trapping.
6. Saves one file – the output NDVI grid - to a workspace other than current workspace.
7. Prints only one message – either script success, user lacks the required extension, or a Level 2 geoprocessing error message.
8. The "script success" message should also report name of output file, its spatial resolution, and units..

## Rubric:

Review the assignment rubric available on Canvas for additional details on how your work will be assessed. Double-check that your script includes a complete header section, uses good commenting, incorporates line spaces between blocks of code, and reads input and writes output to current workspace.

## Submission:

Commit your code changes for <code>GitHub-Rasters.py</code> to your assignment repository on GitHub.
