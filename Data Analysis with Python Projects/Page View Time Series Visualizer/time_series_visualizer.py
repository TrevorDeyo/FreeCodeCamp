import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(r'C:\Users\tdeyo\Desktop\Code\FreeCodeCamp\Data Analysis with Python Projects\Page View Time Series Visualizer\fcc-forum-pageviews.csv')

# Clean data
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Calculate the quantiles for the top and bottom 2.5% of the data
top_quantile = df['value'].quantile(0.975)
bottom_quantile = df['value'].quantile(0.025)

filtered_df = df[(df['value'] > bottom_quantile) & (df['value'] < top_quantile)]

def draw_line_plot():

    # Draw line plot
    fig, ax = plt.subplots(figsize=(32, 10))
    ax.plot(filtered_df.index, filtered_df['value'], color = 'red', linewidth=2.5)
    
    ax.set_xlabel('Date', fontsize = 20)
    ax.set_ylabel('Page Views', fontsize = 20)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019', fontsize = 25)

    ax.tick_params(axis='both', labelsize=20)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = filtered_df.copy()

    # Extract year and month from the index
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    # Group by year and month, then calculate the average page views
    df_bar = df_bar.groupby(['year', 'month']).mean().reset_index()

    # Map month numbers to month names
    month_names = {
        1: 'January', 2: 'February', 3: 'March', 4: 'April',
        5: 'May', 6: 'June', 7: 'July', 8: 'August',
        9: 'September', 10: 'October', 11: 'November', 12: 'December'
    }
    # Map month numbers to month names and define the custom order
    month_order = [
        'January', 'February', 'March', 'April',
        'May', 'June', 'July', 'August',
        'September', 'October', 'November', 'December'
    ]
    df_bar['month'] = pd.Categorical(df_bar['month'].map(month_names), categories=month_order, ordered=True)

    # Pivot table for plotting
    pivot_df = df_bar.pivot(index='year', columns='month', values='value')

    # Create bar plot
    fig, ax = plt.subplots(figsize=(15.14, 13.30))
    pivot_df.plot(kind='bar', ax=ax)

    # Labels & titles
    ax.set_xlabel('Years', fontsize = 20)
    ax.set_ylabel('Average Page Views', fontsize = 20)
    ax.tick_params(axis='both', labelsize=20, which='major', size=10)

    # Legend customizing
    ax.legend(title='Months', title_fontsize=20, fontsize=20)

    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
