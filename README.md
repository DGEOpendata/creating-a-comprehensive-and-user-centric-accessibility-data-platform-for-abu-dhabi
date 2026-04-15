markdown
# Accessibility Data Platform for Abu Dhabi

This repository contains resources and tools for developing a comprehensive accessibility data platform for Abu Dhabi's community infrastructure. The dataset includes detailed information about public facilities and their accessibility features, aiming to improve inclusivity and support urban planning initiatives.

## Features

1. **Dataset**: Includes data on parks, public buildings, recreational centers, and transportation facilities in Abu Dhabi.
2. **Data Points**: 
   - Location
   - Type of facility
   - Accessibility features (e.g., wheelchair ramps, elevators)
   - Operating hours
3. **Formats**: Available in CSV and GeoJSON formats.
4. **Visualization Tools**: Tools for mapping and analyzing accessibility data.

## Prerequisites

- Python 3.8+
- Pandas library
- GeoPandas library
- Matplotlib library

## Installation

1. Clone the repository:
   bash
   git clone https://github.com/YourUsername/AbuDhabiAccessibilityData.git
   
2. Navigate to the repository directory:
   bash
   cd AbuDhabiAccessibilityData
   
3. Install dependencies:
   bash
   pip install pandas geopandas matplotlib
   

## Usage

1. **Load the Dataset**:
   Use the provided Python script to load and analyze the dataset.

2. **Filter Data**:
   Filter the dataset based on your requirements, such as finding wheelchair-accessible facilities.

3. **Visualize Data**:
   Utilize the provided plotting script to visualize the data on a map.

## Example Script

Here is an example of how to use the provided dataset:

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


## Updating the Dataset

1. Ensure data is collected from reliable sources such as government departments, community surveys, and accessibility audits.
2. Perform quality checks to ensure data accuracy and completeness.
3. Update the dataset quarterly with any changes to infrastructure and accessibility features.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

We welcome contributions to this project. Please read the CONTRIBUTING.md file for guidelines on how to contribute.

## Contact

For questions or suggestions, please contact us at: support@abudhabiaccessibilitydata.ae
