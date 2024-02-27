# Author: Jonathan Kasongo (14 / 1 / 23)

# Data visualisation for my school statistics project
# --------------------------------------------------- 
from math import floor
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter

# Get relevant data about the spreadsheet
FILE        = 'MATHS Y8 EOU Tests Tracker 2023-24 - Copy.xlsx'
SHEET_NAME  = 'Year 8'
COL1        = 'X'
COL2        = 'Z'
COL3        = 'AB'

# Parses excel data into a pandas dataframe
Unit_1_data = pd.read_excel( FILE,SHEET_NAME,usecols=COL1,skiprows=122 )[:31]
Unit_2_data = pd.read_excel( FILE,SHEET_NAME,usecols=COL2,skiprows=122 )[:31]
Unit_3_data = pd.read_excel( FILE,SHEET_NAME,usecols=COL3,skiprows=122 )[:31]

# Gets data and parses into a list
def GetData(df) :

    result = []
    for row in range( df.shape[0] ):
        for col in range( df.shape[1] ): result.append( df.iat[row,col] )

    return result

# Easily plot data onto a frequency bar chart
def PlotData(data, name):

    # Get mean, sample standard deviation and variance
    n    = len(data)
    data = sorted(data)
    mean = round( np.mean(data),2 )
    SD   = round( np.std(data, ddof=1),2 )
    var  = round( np.var(data, ddof=1),2 ) 
    Q_1  = data[ floor(0.25*(n+1)) ]
    Q_3  = data[ floor(0.75*(n+1)) ]
    IQR  = Q_3 - Q_1

    # Get x and y axis
    data   = sorted([ (score,freq) for score,freq in Counter(data).items() ])
    X_axis = [ round(score,2) for score,freq in data ]
    Y_axis = [ freq for score,freq in data ]

    # Format the bar char
    plt.bar( X_axis,Y_axis,width = 0.03 )
    plt.xlabel( 'Scores (decimal)' )
    plt.ylabel( 'Frequency' )
    plt.title( f'Test: {name} results' )

    # Show measures of location & spread
    print( f'Test: {name} Mean = {mean} | S.D. = {SD} | Variance = {var}' )
    print( f'Test: {name} Q1 = {Q_1} | IQR = {IQR} | Q3 = {Q_3}' )

    # Show graph
    plt.show()

# Gets a random sample of 20 scores from data
def GetSample(df):

    data   = GetData(df)
    sample = []

    # Iterate 20 times each time getting a random score from the data set
    for i in range(20):

        score = np.random.choice(data)
        sample.append(score)
        data.remove(score)
    
    return sample

# Driver code
if __name__ == '__main__':

    PlotData( GetSample(Unit_1_data),1 )

    PlotData( GetSample(Unit_2_data),2 )

    PlotData( GetSample(Unit_3_data),3 )
