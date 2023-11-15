import matplotlib.pyplot as plt
import pandas as pd


data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Temperature': [25, 28, 30, 32, 31, 29, 27, 26, 26, 27, 27, 24],
    'Rainfall': [50, 40, 60, 30, 70, 45, 55, 60, 65, 70, 40, 45]
}


df = pd.DataFrame(data)


plt.figure(figsize=(8, 6))  
plt.plot(df['Month'], df['Temperature'], marker='o', linestyle='-', color='r')
plt.title('Monthly Temperature Data [LINE PLOT]')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()


plt.figure(figsize=(8, 6))  
plt.scatter(df['Month'], df['Rainfall'], color='b')
plt.title('Monthly Rainfall Data [SCATTER PLOT')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.show()
