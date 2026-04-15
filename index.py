python
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the dataset
csv_file = 'Community_Infrastructure_Accessibility_Data.csv'
data = pd.read_csv(csv_file)

# Convert to a GeoDataFrame for spatial data
geojson_file = 'Community_Infrastructure_Accessibility_Data.geojson'
gdf = gpd.read_file(geojson_file)

# Filter data for wheelchair-accessible recreational centers
wheelchair_accessible = data[(data['Type'] == 'Recreational Center') & (data['Wheelchair Access'] == 'Yes')]

# Get locations for mapping
locations = wheelchair_accessible[['Latitude', 'Longitude']]

# Plot the accessible facilities on a map
base_map = gdf.plot(color='white', edgecolor='black')
locations.plot(kind='scatter', x='Longitude', y='Latitude', color='blue', ax=base_map)
plt.title('Wheelchair Accessible Recreational Centers in Abu Dhabi')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
