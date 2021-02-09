import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mysql.connector
import sys
from datetime import datetime, timedelta
import seaborn as sns

def admt(cst, flow):
    return (cst * flow / 62.5)

def rr(rej, feed):
    return 100 * cst/(cst + feed)

lab = pd.read_csv('labdata.csv')  
samplepoints = pd.read_csv('sample-points.csv')
pidata = pd.read_csv('pidata.csv')


df = lab.join(samplepoints.set_index('sample'), on='sample')
df['admt'] = admt(df.cst, df.flow)
# df['fsrr'] = rr(df.cst, df.flow)

df.to_csv('out.csv')

fsrrm = pd.DataFrame(np.array([[1,0,0],[2,0,0], [3,0,0]]),
                     columns=['trial', 'RRv', 'RRm'])



print(df)
print(df.describe())

print(fsrrm)



# Create plot figure and axis
fig = plt.figure('Screen Audit Feb 3')
ax = fig.add_subplot(1,1,1)

