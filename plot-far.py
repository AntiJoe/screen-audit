import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mysql.connector
import sys
from datetime import datetime, timedelta
import seaborn as sns

df = pd.read_excel('out.xlsx', sheet_name='FAR-csf')

df = df[df.Screen == 'FS']

print(df)
print(df.describe())

trail1 = df[df.Trail == 1]

# Create plot figure and axis
fig = plt.figure('Screen Audit Feb 3')
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }
font['size'] = 12
fig.suptitle('FS Screen \nMass Rejects Rate vs Feed Consistency')

plt.bar(br1, calcs.Frrm, width=barWidth, bottom=0, color='b', label='FS')
plt.bar(br2, calcs.Prrm, width=barWidth, bottom=0, color='g', label='P')
plt.bar(br3, calcs.Srrm, width=barWidth, bottom=0, color='r', label='S')

plt.legend()
# plt.ylim(20, 80)
plt.show()