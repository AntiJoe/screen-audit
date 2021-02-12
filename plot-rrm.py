import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mysql.connector
import sys
from datetime import datetime, timedelta
import seaborn as sns

dff = pd.read_excel('out.xlsx', sheet_name='FAR-con')
print(dff)

dff = dff[dff.Trial != 'SD']

# Create plot figure and axis
fig = plt.figure('Screen Audit Feb 3')
ax = fig.add_subplot(1,1,1)
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }
font['size'] = 12
barWidth = 0.15
fig.suptitle('Reject Rates by Mass vs Feed Consistency\nIndividual and Combined', fontdict=font)
c = ['blue', 'green', 'red', 'black']
m = ['o', '^', 'v', 'D']
offset = [-barWidth, 0, barWidth]
trial= [3,3]
trialLegend = ['Trial 1 - 1.3%', 'Trial 2 - 1.55%', 'Trial 3 - 1.0%']
idx = 0
for screenTag in ['FS', 'P', 'S', 'Combined']:
    df = dff[dff.Screen == screenTag]
    print(df)
    print(df.describe())
    
    # plt.scatter(x=df.feed, y=df.RRm)
    ax = sns.regplot(x=df.feed, y=df.RRm, ci=None, label=screenTag, color=c[idx], marker=m[idx])
    print(idx)
    idx = idx + 1
        
# ax.legend.texts[0].set_text([1,2,3])
plt.legend()
plt.grid(True, ls=':')

plt.xlabel('Feed Consistency (%)', fontdict=font)
plt.ylabel('Reject Rate by Mass', fontdict=font)
xpad = 0.1
ypad = 5
plt.xlim(min(dff.feed) - xpad, max(dff.feed) + xpad)
plt.ylim(min(dff.RRm) - ypad, max(dff.RRm) + ypad)
# plt.yticks(ticks=np.arr)
outfile = 'FPS-rrm.png'
plt.savefig(outfile, dpi=600)
plt.show()
plt.close()