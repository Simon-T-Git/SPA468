#Exercise_9

#print_length.py
import arcpy
arcpy.env.workspace = "C:/PythonPro/Ex09"
fc = "rivers.shp"
with arcpy.da.SearchCursor(fc, ["SHAPE@LENGTH"]) as cursor:
length = 0
for row in cursor:
length = length + row[0]
print(length)

#points.py
import arcpy
arcpy.env.workspace = "C:/PythonPro/Ex09"
fc = "dams.shp"
with arcpy.da.SearchCursor(fc, ["SHAPE@XY"]) as cursor:
for row in cursor:
x, y = row[0]
print("{0:.3f}, {1:.3f}".format(x, y))

#vertices.py
import arcpy
arcpy.env.workspace = "C:/PythonPro/Ex09"
fc = "rivers.shp"
with arcpy.da.SearchCursor(fc, (["OID@", "SHAPE@"])) as cursor:
for row in cursor:
print("Feature {0}: ".format(row[0]))
for point in row[1].getPart(0):
print("{0:.3f}, {1:.3f}".format(point.X, point.Y))

#multipart.py
import arcpy
arcpy.env.workspace = "C:/PythonPro/Ex09"
fc = "dams.shp"
with arcpy.da.SearchCursor(fc, ["OID@", "SHAPE@"]) as cursor:
for row in cursor:
if row[1].isMultipart:
print("Feature {0} is multipart.".format(row[0]))
else:
print("Feature {0} is single part.".format(row[0]))

#multipart_vertices.py
import arcpy
arcpy.env.workspace = "C:/PythonPro/Ex09"
fc = "hawaii.shp"
cursor = arcpy.da.SearchCursor(fc, ["OID@", "SHAPE@"])
for row in cursor:
print("Feature {0}: ".format(row[0]))
partnum = 0
for part in row[1]:
print("Part {0}: ".format(partnum))
for point in part:
print("{0:.2f}, {1:.2f}".format(point.X, point.Y))
partnum += 1

#create_polyline.py
import arcpy
import fileinput
import os
ws = "C:/PythonPro/Ex09"
arcpy.env.workspace = ws
arcpy.env.overwriteOutput = True
newfc = "newpolyline.shp"
arcpy.CreateFeatureclass_management(ws, newfc,"Polyline", spatial_reference = "dams.prj")

#completed
import arcpy
import fileinput
import os
ws = "C:/PythonPro/Ex09"
arcpy.env.workspace = ws
arcpy.env.overwriteOutput = True
newfc = "newpolyline.shp"
arcpy.CreateFeatureclass_management(ws, newfc,"Polyline", spatial_reference = "dams.prj")
infile = os.path.join(ws, "coordinates.txt")
with arcpy.da.InsertCursor(newfc, ["SHAPE@"]) as cursor:
array = arcpy.Array()
for line in fileinput.input(infile):
ID, X, Y = line.split()
array.add(arcpy.Point(X, Y))
cursor.insertRow([arcpy.Polyline(array)])
fileinput.close()

