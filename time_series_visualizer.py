import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import unittest
import matplotlib as mpl
import matplotlib.ticker as mticker
register_matplotlib_converters()
from pandas.plotting import register_matplotlib_converters
from datetime import datetime


def parse_date(x):
    return datetime.strptime(x, "%Y-%m-%d")


# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
file_path=r'/Users/beckyiyeh/Documents/hello_ds./fcc-forum-pageviews.csv'
df = pd.read_csv(file_path,parse_dates=['date'],index_col='date',date_parser=parse_date,
)


# Clean data
df = df.loc[
    (df["value"] >= df["value"].quantile(0.025))
    & (df["value"] <= df["value"].quantile(0.975))
]


def draw_line_plot():
    # Draw line plot
   
    fig,axes= plt.subplots(figsize=(16,6))
    axes=sns.lineplot(data=df, x='date', y='value')
    axes.set_xlabel('Date')
    axes.set_ylabel('Page Views')
    axes.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xticks(rotation=90)
    plt.show()



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy().groupby(pd.Grouper(freq="ME")).mean().rename(columns={'value':'mean'})
    df_bar['year']=pd.DatetimeIndex(df_bar.index).year
    df_bar['month']=pd.DatetimeIndex(df_bar.index).strftime('%B')
    df_bar=pd.melt(df_bar,id_vars=['month','year'],value_vars=['mean'])

    # Draw bar plot
    sns.set_theme(style='dark')
    plt.figure(figsize=(16,6))
    fig=sns.catplot(
        data=df_bar,
        x="year",
        y="value",
        hue="month",
        kind="bar",
        legend=False,)
    fig.set_xlabels("Years")
    fig.set_ylabels("Average Page Views")
    plt.legend(
        title="Months",
        loc="lower right",
        labels=[
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ],
    )

    



    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig.fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy().rename(columns={'value':'views'})
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig,(ax1,ax2)=plt.subplots(1,2,figsize=(20,6))
    sns.boxplot(ax=ax1 , data=df_box, x='year',y='views',label='year')
    ax1.set(xlabel='Year',ylabel='Views',title='Year-wise Box Plot (Trend)')

    sns.boxplot(ax=ax2 , data=df_box, x='month',y='views',label='month', order=[
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ],)
    ax2.set(xlabel='Month',ylabel='Views',title='Year-wise Box Plot (Trend)')
   
   


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig