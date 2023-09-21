import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv(r'C:\Users\tdeyo\Desktop\Code\FreeCodeCamp\Data Analysis with Python Projects\Sea Level Predictor\epa-sea-level.csv')

    # Extract relevant columns
    year = df['Year']
    sea_level = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    plt.scatter(year, sea_level)
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Linear Regression For all data
    slope, intercept, _, _, _ = linregress(year, sea_level)

    # regression line equation for all data
    regression_line = slope * year + intercept

    # Extend regression line to 2050
    future_years = list(range(1880, 2051))
    future_sea_levels = [slope * year + intercept for year in future_years]

    # Plot regression line for all data (historical data)
    plt.plot(year, regression_line, color='red', label='Linear Regression (Historical Data)')

    # plot extended regression line (future prediction)
    plt.plot(future_years, future_sea_levels, linestyle='--', color='green', label='Future Prediction (2050)')

    #linear Regression for data from year 2000 onwards
    recent_data = df[df['Year'] >= 2000]
    recent_year = recent_data['Year']
    recent_sea_level = recent_data['CSIRO Adjusted Sea Level']

    slope_recent, intercept_recent, _, _, _ = linregress(recent_year, recent_sea_level)

    # Regression line equation for data from year 2000 onwardsk
    regression_line_recent = slope_recent * year + intercept_recent

    # Extend regression line to 2050 for data from year 2000 onwards
    future_sea_levels_recent = [slope_recent * year + intercept_recent for year in future_years]

    # Plot regression line for data from year 2000 onwards (historical data)
    plt.plot(year, regression_line_recent, color='blue', label='Linear Regression (Since 2000)')

    # Plot extended regression line for data from year 2000 onwards (future prediction)
    plt.plot(future_years, future_sea_levels_recent, linestyle='--', color='purple', label='Future Prediction (Since 2000)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()