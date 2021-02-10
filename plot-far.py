import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mysql.connector
import sys
from datetime import datetime, timedelta
import seaborn as sns

dffar = pd.read_excel('out.xlsx')
lab = pd.read_csv('labdata.csv')  
samplepoints = pd.read_csv('sample-points.csv')
pidata = pd.read_csv('pidata.csv')
calcs = pd.read_csv('screencalcs.csv')



fsrrm = pd.DataFrame(np.array([[1,0,0],[2,0,0], [3,0,0]]),
                     columns=['trial', 'RRv', 'RRm'])



print(df)
print(df.describe())

print(calcs)
calcs.to_csv('calcs.csv')

# Create plot figure and axis
fig = plt.figure('Screen Audit Feb 3')
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }
font['size'] = 12

fig.suptitle('FS Screen \nMass Rejects Rate vs Feed Consistency')
plt.xlabel('Feed Consistency', fontdict=font)
plt.ylabel('Reject Rate (mass)', fontdict=font)
labels = calcs['Feed.cst']
plt.bar(labels, calcs.Frrm, width=0.1, bottom=0)
# plt.ylim(30, 45)
# plt.show()
# plt.close()
fig = plt.figure('Screen Audit Feb 3')


fig.suptitle('Primary Screen \nMass Rejects Rate vs Feed Consistency')
plt.xlabel('Feed Consistency', fontdict=font)
plt.ylabel('Reject Rate (mass)', fontdict=font)
labels = calcs['Feed.cst']
plt.bar(labels, calcs.Prrm, width=0.1, bottom=0)
# plt.ylim(30, 50)
# plt.show()
# plt.close()
fig = plt.figure('Screen Audit Feb 3')

fig.suptitle('Secondary Screen \nMass Rejects Rate vs Feed Consistency')
plt.xlabel('Feed Consistency', fontdict=font)
plt.ylabel('Reject Rate (mass)', fontdict=font)
labels = calcs['Feed.cst']
plt.bar(labels, calcs.Srrm, width=0.1, bottom=0)
# plt.ylim(50, 80)
# plt.show()
plt.close()


fig = plt.figure('Screen Audit Feb 3')

fig.suptitle('Screen Mass Rejects Rate vs Feed Consistency')
# set width of bar 
barWidth = 0.25

plt.xlabel('Feed Consistency', fontdict=font)
plt.ylabel('Reject Rate (mass)', fontdict=font)


# Set position of bar on X axis 
br1 = np.arange(len(calcs['Trial'])) + 1 - barWidth
br2 = [x + barWidth for x in br1] 
br3 = [x + barWidth for x in br2] 

print(br1)
print(br2)
print(br3)

plt.bar(br1, calcs.Frrm, width=barWidth, bottom=0, color='b', label='FS')
plt.bar(br2, calcs.Prrm, width=barWidth, bottom=0, color='g', label='P')
plt.bar(br3, calcs.Srrm, width=barWidth, bottom=0, color='r', label='S')

# plt.xticks(x, ('1.3 %', '1.55%', '1.0%'))

plt.legend()
plt.ylim(20, 80)
plt.show()

