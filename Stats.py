# Author: Jonathan Kasongo (14 / 1 / 23)

# Data visualisation for my school statistics project
# --------------------------------------------------- 

import matplotlib.pyplot as pyplot
import numpy as np
import pandas as pd

# Parses data into a variables
FILE = 'Test scores tracker.xlsx'

# For the first 20 scores
Test1 = pd.read_excel(FILE, usecols='C2:C22')

# For the next 20 scores
Test2 = pd.read_excel(FILE, usecols='C23:C43')

# For the last 20 scores
Test3 = pd.read_excel(FILE, usecols='C44:C64')