import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('data.csv')

# Display basic information about the dataset
print(data.info())

# Handle missing values (if any)
data.fillna(method='ffill', inplace=True)

# Display the first few rows of the dataset
print(data.head())

# Calculate basic statistics
summary_stats = data.describe()
print(summary_stats)

# Group data by a specific column and calculate mean
grouped_data = data.groupby('Category').mean()
print(grouped_data)

# Identify trends over time (assuming there's a 'Date' column)
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)
monthly_trends = data.resample('M').mean()
print(monthly_trends)

# Plot summary statistics
summary_stats.plot(kind='bar')
plt.title('Summary Statistics')
plt.show()

# Plot grouped data
grouped_data.plot(kind='bar')
plt.title('Average Values by Category')
plt.show()

# Plot trends over time
monthly_trends.plot()
plt.title('Monthly Trends')
plt.show()
