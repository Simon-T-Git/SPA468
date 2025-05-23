#Exercise_11

#projects.py

import arcpy
aprx = arcpy.mp.ArcGISProject("Austin.aprx")
aprx.saveACopy("Austin_Copy.aprx")
del aprx

#list_maps.py

import arcpy
aprx = arcpy.mp.ArcGISProject("Austin.aprx")
m = aprx.listMaps("Region")[0]
m.name = "County"
aprx.saveACopy("Austin_County.aprx")
del aprx

#work_layers.py

import arcpy
aprx = arcpy.mp.ArcGISProject("Austin.aprx")
m = aprx.listMaps("Downtown")[0]
lyrs = m.listLayers()
for lyr in lyrs:
if lyr.isBasemapLayer:
print(lyr.name + " is a basemap layer")
if lyr.isFeatureLayer:
print(lyr.name + " is a feature layer")
del aprx

#layer_symbology.py

import arcpy
aprx = arcpy.mp.ArcGISProject("Austin.aprx")
m = aprx.listMaps("Downtown")[0]
lyr = m.listLayers("parks")[0]
sym = lyr.symbology
red = {"RGB": [100, 175, 0, 100]}
if lyr.isFeatureLayer and hasattr(sym, "renderer"):
sym.renderer.symbol.color = red
lyr.symbology = sym
aprx.saveACopy("Austin_Symbology.aprx")
del aprx
