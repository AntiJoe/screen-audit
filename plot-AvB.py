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

plt.title('PulpEye vs Lab Freeness\n{}'.format(ped['name']), color='firebrick', fontsize=14, fontweight='bold')
ax = sns.regplot(x=pe_cal_old, y=lab_old, ci=None, scatter_kws={'s':dot_size[0]},
 line_kws={'label':"y={0:.2f}x+{1:.2f}".format(slope,intercept)})
ax.set_ylabel("Lab", color='firebrick', fontsize=12, fontweight='bold')
ax.set_xlabel("PulpEye", color='firebrick', fontsize=12, fontweight='bold')