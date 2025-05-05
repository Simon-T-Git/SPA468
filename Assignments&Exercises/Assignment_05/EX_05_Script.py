import arcpy
arcpy.env.workspace = "C:\Users\17692\Desktop\GHY 468\Assignment 05"
arcpy.env.overwriteOutput = True
newclip = arcpy.Clip_analysis("bike_routes.shp", "parks.shp", "bike_clip.shp")
fcount = arcpy.GetCount_management("bike_clip.shp")
msgCount = newclip.messageCount
print(newclip.getMessage(msgCount-1))
in_fc = "parks.shp"
out_fc = "parks_centroid.shp"
if arcpy.ProductInfo() == "ArcInfo":
arcpy.FeatureToPoint_management(in_fc, out_fc)
else:
print("An ArcInfo license is not available.")
