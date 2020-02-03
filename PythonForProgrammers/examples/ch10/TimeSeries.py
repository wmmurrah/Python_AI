# TimeSeries.py

# Function to convert fahrenheit to celsius.
c = lambda f: 5/9 * (f - 32)

temps = [(f, c(f)) for f in range(0, 101, 10)]

import pandas as pd

temps_df = pd.DataFrame(temps, columns=['Fahrenheit', 'Celsius'])

axes = temps_df.plot(x='Fahrenheit', y='Celsius', style='.-')

y_label = axes.set_ylabel('Celsius')

# Import NOAA Data
nyc = pd.read_csv('ave_hi_nyc_jan_1895-2018.csv')

# Rename variables
nyc.columns = ['Date', 'Temperature', 'Anomaly']

# remove last two digits of Date integer
nyc.Date = nyc.Date = nyc.Date.floordiv(100)

# Set decimal places printed
pd.set_option('precision', 2)

nyc.Temperature.describe()

# Forcasting

from scipy import stats

linear_regression = stats.linregress(x=nyc.Date, y=nyc.Temperature)

# Plot regression line

import seaborn as sns

sns.set_style('whitegrid')

axes = sns.regplot(x=nyc.Date, y=nyc.Temperature)

axes.set_ylim(10, 70)
