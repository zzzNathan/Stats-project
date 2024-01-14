# Author: Jonathan Kasongo (14 / 1 / 23)

# Data visualisation for my school statistics project
# --------------------------------------------------- 

import matplotlib.pyplot as pyplot
import numpy as np
import pandas as pd

# Parses data into a variable
FILE = 'Test scores tracker.xlsx'
data = pd.read_excel(FILE, usecols='C:C')