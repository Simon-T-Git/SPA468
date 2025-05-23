#Assignment_09

import arcpy

# Get input parameters
watershed_fc = arcpy.GetParameterAsText(0)  # Feature class representing watersheds
watershed_id_field = arcpy.GetParameterAsText(1)  # Field representing unique ID for watersheds
census_fc = arcpy.GetParameterAsText(2)  # Feature class representing census tracts
population_field = arcpy.GetParameterAsText(3)  # Field representing population in census tracts
output_fc = arcpy.GetParameterAsText(4)  # Location of the output feature class

# Step 1: Dissolve watersheds based on the unique ID field
# Use in_memory for temporary storage to improve performance
dissolved_watersheds = arcpy.Dissolve_management(
    in_features=watershed_fc,
    out_feature_class="in_memory/dissolved_watersheds",
    dissolve_field=watershed_id_field
)

# Step 2: Summarize population within dissolved watersheds
arcpy.SummarizeWithin_analysis(
    in_polygons=dissolved_watersheds,
    in_sum_features=census_fc,
    out_feature_class=output_fc,
    sum_fields=[population_field],
    keep_all_polygons="KEEP_ALL_POLYGONS"  # Include watersheds with no overlapping census tracts
)

# Script completion message
arcpy.AddMessage("Script completed successfully. Output saved to: " + output_fc)
