import arcpy

# Set workspace (path to your geodatabase or folder containing the tornado data)
arcpy.env.workspace = "C:/path/to/your/workspace"

# Input tornado feature class (name of your tornado dataset)
tornado_fc = "TornadoData"

# Add new "Month" field as string
arcpy.AddField_management(tornado_fc, "Month", "TEXT", field_length=20)

# Dictionary to map integer months to string names
month_dict = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}

# Update the "Month" field with string month names based on "mo" field
with arcpy.da.UpdateCursor(tornado_fc, ["mo", "Month"]) as cursor:
    for row in cursor:
        month_num = row[0]  # mo field (integer)
        if month_num in month_dict:
            row[1] = month_dict[month_num]  # Set Month field to string
            cursor.updateRow(row)

# Create summary statistics table for tornado count by month
output_table = "Tornado_Month_Summary"
arcpy.Statistics_analysis(
    in_table=tornado_fc,
    out_table=output_table,
    statistics_fields=[["Month", "COUNT"]],
    case_field=["Month"]
)

print("Script completed. Summary table created: " + output_table)
