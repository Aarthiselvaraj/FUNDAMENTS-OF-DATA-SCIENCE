import pandas as pd

data = {
    'Property_ID': [1, 2, 3, 4, 5],
    'Location': ['Location_A', 'Location_B', 'Location_A', 'Location_C', 'Location_B'],
    'Bedrooms': [3, 4, 5, 4, 6],
    'Area_SqFt': [1500, 2000, 2500, 1800, 3000],
    'Listing_Price': [200000, 300000, 400000, 250000, 500000]
}

property_data = pd.DataFrame(data)
average_price_per_location = property_data.groupby('Location')['Listing_Price'].mean()
print(average_price_per_location)

properties_more_than_four_beds = property_data[property_data['Bedrooms'] > 4]
num_properties_more_than_four_beds = len(properties_more_than_four_beds)
print(num_properties_more_than_four_beds)

property_with_largest_area = property_data[property_data['Area_SqFt'] == property_data['Area_SqFt'].max()]
print(property_with_largest_area)
