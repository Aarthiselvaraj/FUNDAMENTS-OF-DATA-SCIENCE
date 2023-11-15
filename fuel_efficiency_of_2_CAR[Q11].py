import numpy as np


fuel_efficiency = np.array([25, 30, 28, 32, 27, 29, 31, 33, 26, 30])


average_fuel_efficiency = np.mean(fuel_efficiency)
print(f"The average fuel efficiency is: {average_fuel_efficiency} miles per gallon")

car_model_1 = 25
car_model_2 = 30


percentage_improvement = ((car_model_2 - car_model_1) / car_model_1) * 100
print(f"The percentage improvement between car model 1 and car model 2 is: {percentage_improvement:.2f}%")
