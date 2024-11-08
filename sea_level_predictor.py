import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(x=df['Year'],y=df['CSIRO Adjusted Sea Level'], s=50,cmap='Red')



    # Create first line of best fit
    slope,intercept,r_value,_,_ =linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    x=np.arange(df['Year'].min(),2051)
    line_of_best_fit=slope*x+intercept
    plt.plot(x,line_of_best_fit,color='purple',linestyle='dotted', label='best fit')

    # Create second line of best fit
    two_df=df[df['Year']>= 2000]
    slope2,intercept2,r_value2,_,_ =linregress(two_df['Year'],two_df['CSIRO Adjusted Sea Level'])
    y=np.arange(2000,2051)
    line_of_best_fit2000=slope2* y +intercept2
    plt.plot(y,line_of_best_fit2000,'b--',label="Best Fit Line (2000 Onwards)")

    # Add labels and title
    plt.legend()

    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Sea Level Rise Prediction")


    plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
