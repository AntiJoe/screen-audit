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

for screenTag in ['FS', 'P', 'S']:
    df = dff[dff.Screen == screenTag]
    print(df)
    print(df.describe())
    


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
    fig.suptitle('{} Screen \nFreeness Streams vs Feed Consistency'.format(screenTag))
    c = ['b', 'g', 'r']
    offset = [-barWidth, 0, barWidth]
    trial= [3,3]
    trialLegend = ['Trial 1 - 1.3%', 'Trial 2 - 1.55%', 'Trial 3 - 1.0%']

    # plt.scatter(x=df.feed, y=df.RRm)
    ax = sns.regplot(x=df.feed, y=df.RRm, ci=None)
        
    # ax.legend.texts[0].set_text([1,2,3])
    # plt.legend()
    plt.grid(True, ls=':')
    
    plt.xlabel('Feed Consistency (%)', fontdict=font)
    plt.ylabel('Reject Rate by Mass', fontdict=font)
    xpad = 0.1
    ypad = 1
    plt.xlim(min(df.feed) - xpad, max(df.feed) + xpad)
    plt.ylim(min(df.RRm) - ypad, max(df.RRm) + ypad)
    # plt.yticks(ticks=np.arr)
    outfile = '{}-con-rrm.png'.format(screenTag)
    plt.savefig(outfile, dpi=600)
    plt.show()
    plt.close()