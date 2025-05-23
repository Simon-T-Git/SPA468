#Exercise_08

#print_values.py
import arcpy
arcpy.env.workspace = "C:/PythonPro/Ex06"
fc = "airports.shp"
cursor = arcpy.da.SearchCursor(fc, ["NAME"])
for row in cursor:
print("Airport name = {0}".format(row[0]))

#sql.py
import arcpy
arcpy.env.workspace = "C:/PythonPro/Ex08"
fc = "airports.shp"
sql_exp = '"TOT_ENP" > 100000'
cursor = arcpy.da.SearchCursor(fc, ["NAME"], sql_exp)
for row in cursor:
print(row[0])

#select.py
import arcpy
arcpy.env.workspace = "C:/PythonPro/Ex08"
infc = "airports.shp"
outfc = "airports_anchorage.shp"
delim_field = arcpy.AddFieldDelimiters(infc, "COUNTY")
sql_exp = delim_field + " = 'Anchorage Borough'"
arcpy.Select_analysis(infc, outfc, sql_exp)

#update.py
import arcpy
arcpy.env.workspace = "C:/PythonPro/Ex08"
fc = "airports.shp"
delimfield = arcpy.AddFieldDelimiters(fc, "STATE")
sql_exp = delimfield + " <> 'AK'"
with arcpy.da.UpdateCursor(fc, ["STATE"], sql_exp) as cursor:
for row in cursor:
row[0] = "AK"
cursor.updateRow(row)

#delete.py
import arcpy
arcpy.env.workspace = "C:/PythonPro/Ex08"
fc = "airports.shp"
with arcpy.da.UpdateCursor(fc, ["TOT_ENP"]) as cursor:
for row in cursor:
if row[0] < 100000:
cursor.deleteRow()

#insert.py
import arcpy
arcpy.env.workspace = "C:/PythonPro/Ex08"
fc = "airports.shp"
with arcpy.da.InsertCursor(fc, "NAME") as cursor:
cursor.insertRow(["New Airport"])

#validate.py
import arcpy
arcpy.env.workspace = "C:/PythonPro/Ex08"
fc = "airports.shp"
newfield = "NEW CODE"
fieldtype = "TEXT"
fieldname = arcpy.ValidateFieldName(newfield)
arcpy.AddField_management(fc, fieldname, fieldtype, "", "", 12)

#unique_name.py
import arcpy
arcpy.env.workspace = "C:/PythonPro/Ex08"
fc = "airports.shp"
unique_name = arcpy.CreateUniqueName("buffer.shp")
arcpy.Buffer_analysis(fc, unique_name, "5000 METERS")

