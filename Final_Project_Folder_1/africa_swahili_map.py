import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import matplotlib.patches as patches
import uuid

# Dictionary of African country names in Swahili (ISO 3166-1 alpha-2 codes to Swahili names)
swahili_names = {
    'DZ': 'Aljeria', 'AO': 'Angola', 'BJ': 'Benin', 'BW': 'Botswana', 'BF': 'Burkina Faso',
    'BI': 'Burundi', 'CM': 'Kameruni', 'CV': 'Kepuvede', 'CF': 'Jamhuri ya Afrika ya Kati',
    'TD': 'Chadi', 'KM': 'Komoro', 'CD': 'Jamhuri ya Kidemokrasia ya Kongo',
    'CG': 'Kongo', 'CI': "Côte d'Ivoire", 'DJ': 'Jibuti', 'EG': 'Misri',
    'GQ': 'Ginekweta', 'ER': 'Eritrea', 'ET': 'Ethiopia', 'GA': 'Gabon',
    'GM': 'Gambia', 'GH': 'Ghana', 'GN': 'Gine', 'GW': 'Ginebisau', 'KE': 'Kenya',
    'LS': 'Lesotho', 'LR': 'Liberia', 'LY': 'Libya', 'MG': 'Madagaska', 'MW': 'Malawi',
    'ML': 'Mali', 'MR': 'Moritania', 'MU': 'Morisi', 'MA': 'Moroko', 'MZ': 'Msumbiji',
    'NA': 'Namibia', 'NE': 'Nijeri', 'NG': 'Nigeria', 'RE': 'Riyunioni', 'RW': 'Rwanda',
    'ST': 'Sao Tome na Prinsipe', 'SN': 'Senegali', 'SC': 'Shelisheli', 'SL': 'Siera Leoni',
    'SO': 'Somalia', 'ZA': 'Afrika Kusini', 'SS': 'Sudani Kusini', 'SD': 'Sudani',
    'SZ': 'Eswatini', 'TG': 'Togo', 'TN': 'Tunisia', 'UG': 'Uganda', 'EH': 'Sahara Magharibi',
    'ZM': 'Zambia', 'ZW': 'Zimbabwe'
}

# Load the shapefile for African countries
world = gpd.read_file('ne_110m_admin_0_countries.shp')

# Filter for African countries
africa = world[world['CONTINENT'] == 'Africa']

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 12))

# Plot the map with country boundaries
africa.plot(ax=ax, color='lightgreen', edgecolor='black')

# Loop through each country to add Swahili labels
for idx, row in africa.iterrows():
    country_code = row['ISO_A2']
    # Branching: Check if Swahili name exists; use English name if not
    if country_code in swahili_names:
        label = swahili_names[country_code]
    else:
        label = row['NAME']
        print(f"Warning: No Swahili name for {row['NAME']}, using English name.")

    # Get the centroid of the country for label placement
    centroid = row.geometry.centroid
    x, y = centroid.x, centroid.y

    # Branching: Adjust label position for specific countries to avoid overlap
    if country_code in ['CV', 'SC', 'KM', 'MU', 'ST']:
        x_offset = 1.0
        y_offset = 0.5
    elif country_code == 'ZA':
        x_offset = 0
        y_offset = -1.0
    else:
        x_offset = 0
        y_offset = 0

    # Add the label with a white outline
    ax.text(
        x + x_offset, y + y_offset, label, fontsize=8, ha='center',
        path_effects=[pe.withStroke(linewidth=2, foreground='white')]
    )

# Set map titles
ax.set_title('Ramani ya Afrika kwa Kiswahili', fontsize=14, pad=20)
ax.text(0.5, 0.95, 'Map of Africa in Swahili', fontsize=12, ha='center', transform=ax.transAxes)

# Add scale bar (approximate, assuming 1 degree ~ 111 km)
scale_length_km = 1000  # 1000 km
scale_length_deg = scale_length_km / 111  # Convert km to degrees
scale_x, scale_y = -15, -35  # Position in lower-left
ax.add_patch(patches.Rectangle((scale_x, scale_y), scale_length_deg, 0.5, facecolor='black'))
ax.text(scale_x + scale_length_deg / 2, scale_y + 0.7, '1000 km', fontsize=8, ha='center')

# Add north arrow
arrow_x, arrow_y = 45, -30  # Position in lower-right
ax.arrow(arrow_x, arrow_y, 0, 2, head_width=1, head_length=1, fc='black', ec='black')
ax.text(arrow_x, arrow_y + 2.5, 'N', fontsize=10, ha='center')

# Add signature
ax.text(0.5, 0.02, 'GHY 468 Final Project by: Simon Tipton', fontsize=8, ha='center', transform=ax.transAxes)

# Remove axes
ax.set_axis_off()

# Save the map as a PNG
output_file = f'africa_swahili_map_{uuid.uuid4().hex}.png'
plt.savefig(output_file, dpi=300, bbox_inches='tight')
plt.close()

print(f"Map saved as {output_file}")