# Author: Jonathan Kasongo (14 / 1 / 23)

# Data visualisation for my school statistics project
# --------------------------------------------------- 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter

# Parses data into a variables
FILE        = 'MATHS Y8 EOU Tests Tracker 2023-24 - Copy.xlsx'
SHEET_NAME  = 'Year 8'
Unit_1_data = pd.read_excel( FILE,SHEET_NAME,usecols='X',skiprows=122 )[:31]
Unit_2_data = pd.read_excel( FILE,SHEET_NAME,usecols='Z',skiprows=122 )[:31]
Unit_3_data = pd.read_excel( FILE,SHEET_NAME,usecols='AB',skiprows=122 )[:31]

# Gets data and parses into a list
def GetData( df ):

    result = []
    for row in range( df.shape[0] ):
        for col in range( df.shape[1] ): result.append( df.iat[row,col] )

    return result

# Easily plot data onto a frequency bar chart
def PlotData( data ):

    # Get x and y axis
    print(data)
    data   = sorted([(score,freq) for score,freq in  Counter(data).items() ])
    X_axis = [ round(score,2) for score,freq in data ]
    Y_axis = [ freq for score,freq in data ]

    # Format the bar char
    plt.bar( X_axis,Y_axis,width = 0.03 )
    plt.xlabel( 'Scores (decimal)' )
    plt.ylabel( 'Frequency' )
    plt.title( 'Test results' )

    plt.show()

# Gets a random sample of 20 scores from data
def GetSample( df ):

    data   = GetData( df )
    sample = []

    # Iterate 20 times each time getting a random score from the data set
    for i in range(20):

        score = np.random.choice( data )
        sample.append( score )
        data.remove( score )
    
    return sample

PlotData( GetSample(Unit_1_data) )

PlotData( GetSample(Unit_2_data) )

PlotData( GetSample(Unit_3_data) )