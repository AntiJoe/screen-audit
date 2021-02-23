import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mysql.connector
import sys
from datetime import datetime, timedelta
import seaborn as sns
from scipy import stats

dff = pd.read_excel('out.xlsx', sheet_name='FAR-con')
print(dff) # print out datafile

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
fig.suptitle('Screen Freeness Drop vs Feed Consistency\nIndividual Screens and Combined Screenroom', fontdict=font)
c = ['blue', 'green', 'red', 'black']
m = ['o', '^', 'v', 'D']
w = [2,2,2,2]
ls = ['--', '--', '--', '-']
offset = [-barWidth, 0, barWidth]
trial= [3,3]
trialLegend = ['Trial 1 - 1.3%', 'Trial 2 - 1.55%', 'Trial 3 - 1.0%']
idx = 0
for screenTag in ['FS', 'P', 'S', 'Combined']:
    df = dff[dff.Screen == screenTag]
    print(df)
    print(df.describe())
    
    # plt.scatter(x=df.feed, y=df.RRm)
    ax = sns.regplot(x=df.feed, y=df.CSFdrop, ci=None, label=screenTag, color=c[idx], 
    marker=m[idx], line_kws={"lw":w[idx], "ls": ls[idx]})
    print(idx)
    idx = idx + 1

slope, intercept, r_value, p_value, std_err = stats.linregress(df.feed, df.RRm) 
print('slope: {}, intercept: {}, r_squ: {}, p_value: {}, std_err: {}'.format(slope, intercept, r_value**2, p_value, std_err))

# ax.legend.texts[0].set_text([1,2,3])
plt.legend()
plt.grid(True, ls=':')

plt.xlabel('Feed Consistency', fontdict=font)
plt.ylabel('Freeness Drop (ml)', fontdict=font)
xpad = 0.1
ypad = 5
plt.xlim(min(dff.feed) - xpad, max(dff.feed) + xpad)
plt.ylim(min(dff.CSFdrop) - ypad, max(dff.CSFdrop) + ypad)
# plt.yticks(ticks=np.arr)
outfile = '{}-csfdrop-cst.png'.format(screenTag)
plt.savefig(outfile, dpi=600)
plt.show()
plt.close()
