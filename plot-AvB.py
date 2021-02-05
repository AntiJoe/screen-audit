import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mysql.connector
import sys
from datetime import datetime, timedelta
import seaborn as sns

def admt(cst, flow):
    return (cst * flow)

def rr(rej, feed):
    return 100 * cst/(cst + feed)

lab = pd.read_csv('labdata.csv')  
samplepoints = pd.read_csv('sample-points.csv')

df = lab.join(samplepoints.set_index('sample'), on='sample')
df['admt'] = admt(df.cst, df.flow)
# df['fsrr'] = rr(df.cst, df.flow)

print(df)
print(df.describe())



# Create plot figure and axis
fig = plt.figure('Screen Audit Feb 3')
ax = fig.add_subplot(1,1,1)

