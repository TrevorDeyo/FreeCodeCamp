import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv(r'C:\Users\tdeyo\Desktop\Code\FreeCodeCamp\Data Analysis with Python Projects\Sea Level Predictor\sea_level_predictor.py')

    # Create scatter plot
    plt.scatter(df)

    # Add labels and a title
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')
    plt.title('Scatter Plot Example')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x, y)


    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()