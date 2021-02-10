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
calcs = pd.read_csv('screencalcs.csv')

df = lab.join(samplepoints.set_index('sample'), on='sample')
df['admt'] = admt(df.cst, df.flow)
# df['fsrr'] = rr(df.cst, df.flow)

df.to_csv('out.csv')

fsrrm = pd.DataFrame(np.array([[1,0,0],[2,0,0], [3,0,0]]),
                     columns=['trial', 'RRv', 'RRm'])



print(df)
print(df.describe())

print(calcs)



# Create plot figure and axis
fig = plt.figure('Screen Audit Feb 3')
ax = fig.add_subplot(1,1,1)

fig.suptitle('Screen Audit Feb 3, 2021')
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }

# plt.title('Quality Window\n' + start_time + ' --  ' + end_time, fontdict=font, loc='left')
# plt.legend(['MC6', 'MC1', 'Rejects', 'L1', 'L2', 'L3'])

font['size'] = 12
plt.xlabel('Trial', fontdict=font)
plt.ylabel('Reject Rate (mass)', fontdict=font)

plt.style.use('seaborn-dark-palette')
# plt.scatter(x=calcs['Feed.cst'], y=calcs.Frrm, s=9, c='black', marker='o')
ax.bar(calcs['Trial'], calcs.Frrm, width=0.25, bottom=0)
# plt.ylim(0, 100)

plt.show()