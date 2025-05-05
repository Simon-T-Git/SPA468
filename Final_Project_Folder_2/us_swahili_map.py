import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import matplotlib.patches as patches
import uuid

# Dictionary of U.S. state names in Swahili
swahili_names = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'Kalifonia',
    'CO': 'Kolorado', 'CT': 'Konektikati', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Jojia',
    'HI': 'Hawai', 'ID': 'Idaho', 'IL': 'Ilinoi', 'IN': 'Indiana', 'IA': 'Iowa',
    'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
    'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi',
    'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire',
    'NJ': 'New Jersey', 'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina',
    'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania',
    'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee',
    'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont', 'VA': 'Virginia', 'WA': 'Washington',
    'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'
}

# Load the shapefile for U.S. states
shapefile_path = r'C:\Users\17692\Desktop\GHY 468\Final Project\Final Project 2\ne_110m_admin_1_states_provinces.shp'
us_states = gpd.read_file(shapefile_path)

# Filter for U.S. states
us_states = us_states[us_states['iso_a2'] == 'US']

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the map with state boundaries
us_states.plot(ax=ax, color='lightblue', edgecolor='black')

# Loop through each state to add Swahili labels
for idx, row in us_states.iterrows():
    state_code = row['postal']
    # Branching: Check if Swahili name exists; use English name if not
    if state_code in swahili_names:
        label = swahili_names[state_code]
    else:
        label = row['name']
        print(f"Warning: No Swahili name for {row['name']}, using English name.")

    # Get the centroid of the state for label placement
    centroid = row.geometry.centroid
    x, y = centroid.x, centroid.y

    # Branching: Adjust label position for specific states to avoid overlap
    if state_code in ['RI', 'DE', 'CT']:
        x_offset = 0.5
        y_offset = 0.2
    elif state_code == 'AK':
        x_offset = -5.0
        y_offset = -3.0
    elif state_code == 'HI':
        x_offset = 2.0
        y_offset = 1.0
    else:
        x_offset = 0
        y_offset = 0

    # Add the label with a white outline
    ax.text(
        x + x_offset, y + y_offset, label, fontsize=6, ha='center',
        path_effects=[pe.withStroke(linewidth=2, foreground='white')]
    )

# Set map titles
ax.set_title('Ramani ya Marekani kwa Kiswahili', fontsize=14, pad=20)
ax.text(0.5, 0.95, 'Map of the United States in Swahili', fontsize=12, ha='center', transform=ax.transAxes)

# Add scale bar (approximate, assuming 1 degree ~ 111 km)
scale_length_km = 1000  # 1000 km
scale_length_deg = scale_length_km / 111  # Convert km to degrees
scale_x, scale_y = -120, 25  # Position in lower-left
ax.add_patch(patches.Rectangle((scale_x, scale_y), scale_length_deg, 0.3, facecolor='black'))
ax.text(scale_x + scale_length_deg / 2, scale_y + 0.5, '1000 km', fontsize=8, ha='center')

# Add north arrow
arrow_x, arrow_y = -70, 25  # Position in lower-right
ax.arrow(arrow_x, arrow_y, 0, 2, head_width=1, head_length=1, fc='black', ec='black')
ax.text(arrow_x, arrow_y + 2.5, 'N', fontsize=10, ha='center')

# Add signature
ax.text(0.5, 0.02, 'GHY 468 Final Project by: Simon Tipton', fontsize=8, ha='center', transform=ax.transAxes)

# Remove axes
ax.set_axis_off()

# Save the map as a PNG
output_file = f'us_swahili_map_{uuid.uuid4().hex}.png'
plt.savefig(output_file, dpi=300, bbox_inches='tight')
plt.close()

print(f"Map saved as {output_file}")