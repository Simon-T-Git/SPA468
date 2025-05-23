#Exercise_10

#list_rasters.py
import arcpy
arcpy.env.workspace = "C:/PythonPro/Ex10"
rasterlist = arcpy.ListRasters()
for raster in rasterlist:
print(raster)

#describe_rasters.py
import arcpy
arcpy.env.workspace = "C:/PythonPro/Ex10"
raster = "tm.img"
desc = arcpy.da.Describe(raster)
print("Raster base name: " + desc["baseName"])
print("Raster data type: " + desc["dataType"])
print("Raster file extension: " + desc["extension"])

#modify
import arcpy
arcpy.env.workspace = "C:/PythonPro/Ex10"
raster = "landcover.tif"
desc = arcpy.da.Describe(raster)
x = desc["meanCellHeight"]
y = desc["meanCellWidth"]
spatialref = desc["spatialReference"]
units = spatialref.linearUnitName
print("The raster resolution is {0} by {1} {2}.".format(x, y, units))

#modify
import arcpy
arcpy.env.workspace = "C:/PythonPro/Ex10"
raster = "tm.img"
desc = arcpy.da.Describe(raster)
for rband in desc["children"]:
bandname = rband["baseName"]
x = rband["meanCellHeight"]
y = rband["meanCellWidth"]
spatialref = desc["spatialReference"]
units = spatialref.angularUnitName
print("The resolution of {0} is {1:.7f} by {2:.7f} {3}."
.format(bandname, x, y, units))

#raster_objects.py
import arcpy
arcpy.env.workspace = "C:/PythonPro/Ex10"
outraster = arcpy.sa.Slope("elevation")
outraster.save("slope")

#raster_algerbra.py
import arcpy
from arcpy.sa import *
arcpy.env.workspace = "C:/PythonPro/Ex10"
elevraster = arcpy.Raster("elevation")
slope = Slope(elevraster)
goodslope = slope < 20
goodelev = elevraster < 2500
goodfinal = goodslope & goodelev
goodfinal.save("final")

#reclass.py
import arcpy
from arcpy.sa import *
arcpy.env.workspace = "C:/PythonPro/Ex10"
myremap = RemapValue([[41,1], [42,2], [43,3]])
outreclass = Reclassify("landcover.tif", "VALUE", myremap, "NODATA")
outreclass.save("lc_recl")


