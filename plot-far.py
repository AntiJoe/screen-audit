import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mysql.connector
import sys
from datetime import datetime, timedelta
import seaborn as sns

df = pd.read_excel('out.xlsx', sheet_name='FAR-csf')
print(df)

screenTag = 'FS'

df = df[df.Screen == screenTag]
print(df)
print(df.describe())

# Create plot figure and axis
fig = plt.figure('Screen Audit Feb 3')
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }
font['size'] = 12
barWidth = 0.15
fig.suptitle('{} Screen \nFreeness Streams vs Feed Consistency'.format(screenTag))
c = ['b', 'g', 'r']
offset = [-barWidth, 0, barWidth]
trial= [3,3]
trialLegend = ['Trial 1 - 1.3%', 'Trial 2 - 1.55%', 'Trial 3 - 1.0%']

for i in [1,2,3]:
  trial = df[df.Trial == i]
  plt.bar(1 + offset[i -1], trial.feed, width=barWidth, bottom=0, color=c[i-1], label=trialLegend[i-1])
  plt.bar(2 + offset[i -1], trial.accepts, width=barWidth, bottom=0, color=c[i-1])
  plt.bar(3 + offset[i -1], trial.rejects, width=barWidth, bottom=0, color=c[i-1])

plt.legend()
plt.grid(True, ls=':')
plt.xticks([1,2,3], labels=['Feed', 'Accepts', 'Rejects'])
plt.ylabel('Freeness (ml)', fontdict=font)

plt.show()