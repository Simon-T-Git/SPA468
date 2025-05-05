#Exercise_6_shape_exists

import arcpy
arcpy.env.workspace = "C:/PythonPro/Ex06"
shp_exists = arcpy.Exists("cities.shp")
print(shp_exists)

import arcpy
arcpy.env.workspace = "C:/PythonPro/Ex06"
fc = "cities.shp"
newfc = "cities_copy.shp"
if arcpy.Exists(fc):
arcpy.CopyFeatures_management(fc, newfc)

myshp = arcpy.da.Describe("C:/PythonPro/Ex06/cities.shp")
myshp["dataType"]

myshp["datasetType"]

myshp["catalogPath"]

myshp["file"]

myshp["shapeType"]

myshp["spatialReference"]

myshp["spatialReference"].name

myshp["spatialReference"].type

#Exercise_6_list_data

import arcpy
arcpy.env.workspace = "C:/PythonPro/Ex06"
fclist = arcpy.ListFeatureClasses()
print(fclist)

import arcpy
arcpy.env.workspace = "C:/PythonPro/Ex06"
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
fcdesc = arcpy.da.Describe(fc)
dtype = fcdesc["dataType"]
name = fcdesc["name"]
stype = fcdesc["shapeType"]
print(f"{dtype} {name} has shapetype {stype}")

import arcpy
import os
ws = "C:/PythonPro/Ex06"
fgdb = "Copy.gdb"
arcpy.CreateFileGDB_management(ws, fgdb)
arcpy.env.workspace = ws
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
fcname = arcpy.da.Describe(fc)["baseName"]
newfc = os.path.join(ws, fgdb, fcname)
arcpy.CopyFeatures_management(fc, newfc)

#Exercise_6_list_fields

import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:/PythonPro/Ex06"
fieldlist = arcpy.ListFields("cities.shp")
for field in fieldlist:
print(field.name + " " + field.type)

#Exercise_6_mainpulate_lists

arcpy.env.workspace = "C:/PythonPro/Ex06/Copy.gdb"
fclist = arcpy.ListFeatureClasses()
print(fclist)

fclist[0]

fclist[3]

fclist[-1]

fclist[1:3]

fclist[2:]

cities = ["Alameda", "Brazos", "Chimayo", "Dulce"]

len(cities)

del cities[2]
print(cities)

cities.sort(reverse = True)
print(cities)

cities.sort()
print(cities)

"Zuni" in cities

cities.append("Zuni")
print(cities)

cities.insert(0,"Espanola")
print(cities)

countylookup = {"Alameda": "Bernalillo County", "Brazos": "Rio Arriba County", "Chimayo": "Santa Fe County"}

countylookup["Brazos"]

countylookup["Santa Fe County"]

len(countylookup)

list(countylookup.keys())

list(countylookup.values())










