import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mysql.connector
import sys
from datetime import datetime, timedelta
import seaborn as sns

dff = pd.read_excel('out.xlsx', sheet_name='FAR-csf')
print(dff)



for screenTag in ['FS', 'P', 'S', 'Combined']:
    df = dff[dff.Screen == screenTag]
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
    fig.suptitle('{} Screen \nFreeness Streams vs Feed Consistency'.format(screenTag), fontdict=font)
    c = ['b', 'g', 'r', 'cyan', 'orange']
    baralpha = 0.8
    # offset = [0, barWidth, -barWidth, 2*barWidth, 3*barWidth]
    # offset = [-barWidth, 0, -2*barWidth, barWidth, 2*barWidth]
    offset = [barWidth, 2*barWidth, -2*barWidth, 0, -1*barWidth]
    trial= [3,3]
    trialLegend = ['Trial 1 - 1.3%', 'Trial 2 - 1.55%', 'Trial 3 - 1.0%', 'Trial 4 - 1.2%', 'Trial 5 - 1.1%']

    for i in [1,2,3,4,5]:
        trial = df[df.Trial == i]
        plt.bar(1 + offset[i -1], trial.feed, width=barWidth, bottom=0, alpha=baralpha, color=c[i-1], label=trialLegend[i-1])
        plt.bar(2 + offset[i -1], trial.accepts, width=barWidth, bottom=0, alpha=baralpha, color=c[i-1])
        plt.bar(3 + offset[i -1], trial.rejects, width=barWidth, bottom=0, alpha=baralpha, color=c[i-1])

    plt.legend()
    plt.grid(True, ls=':')
    plt.xticks([1,2,3], labels=['Feed', 'Accepts', 'Rejects'])
    plt.ylabel('Freeness (ml)', fontdict=font)
    # plt.yticks(ticks=np.arr)
    outfile = '{}-csf-far.png'.format(screenTag)
    plt.savefig(outfile, dpi=600)
    plt.show()
    plt.close()
