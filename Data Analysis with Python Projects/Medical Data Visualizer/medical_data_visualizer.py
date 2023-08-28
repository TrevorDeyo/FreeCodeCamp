import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv(r"C:\Users\tdeyo\Desktop\Code\FreeCodeCamp\Data Analysis with Python Projects\Medical Data Visualizer\medical_examination.csv")

# Add 'overweight' column

# get height in meters then squared
df['height_in_meters'] = df['height'] / 100

# calculate BMI
df['BMI'] = df['weight'] / (df['height_in_meters'] ** 2)

df['overweight'] = (df['BMI'] > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
chol_gluc_normalizing = ['cholesterol', 'gluc']
df[chol_gluc_normalizing] = df[chol_gluc_normalizing].applymap(lambda x: 0 if x == 1 else 1 if x > 1 else 0)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    cat = df['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    df_cat = pd.melt(df[cat])

    print(df_cat)

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = None
    

    # Draw the catplot with 'sns.catplot()'



    # Get the figure for the output
    fig = None


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None



    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
