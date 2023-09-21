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
    fig, ax = plt.subplots()
    plt.scatter(year, sea_level)

    # Create first line of best fit
    res = linregress(year, sea_level)
    year_prediction = pd.Series([i for i in range(1880,2051)])
    sea_level_prediction = res.slope * year_prediction + res.intercept
    plt.plot(year_prediction, sea_level_prediction, "r")

    # Create second line of best fit
    new_df = df.loc[df['Year'] >= 2000]
    future_years_prediction = new_df['Year']
    future_sea_level_prediction = new_df["CSIRO Adjusted Sea Level"]
    res_2 = linregress(future_years_prediction, future_sea_level_prediction)
    x_pred2 = pd.Series([i for i in range(2000,2051)])
    y_pred2 = res_2.slope * x_pred2 + res_2.intercept
    plt.plot(x_pred2, y_pred2, 'green')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()