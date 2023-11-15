import numpy as np
import csv


sample_data = np.array([
    [5, 2000, 300000],  
    [4, 1800, 250000],  
    [6, 2200, 350000],  
    [5, 2100, 320000],  
    [4, 1900, 260000]   
])


with open('house_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(sample_data)


house_data = np.genfromtxt('house_data.csv', delimiter=',')


houses_more_than_4_bedrooms = house_data[house_data[:, 0] > 4]  


sale_prices_more_than_4_bedrooms = houses_more_than_4_bedrooms[:, -1]  


average_price_more_than_4_bedrooms = np.mean(sale_prices_more_than_4_bedrooms)
print(f"The average sale price of houses with more than four bedrooms INR-{average_price_more_than_4_bedrooms:.2f}")
