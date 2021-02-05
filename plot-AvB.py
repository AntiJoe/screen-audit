import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mysql.connector
import sys
from datetime import datetime, timedelta
import seaborn as sns

def admt(cst, flow):
    return (cst * flow)

lab = pd.read_csv('labdata.csv')  
samplepoints = pd.read_csv('sample-points.csv')

df = lab.join(samplepoints.set_index('sample'), on='sample')
df['admt'] = admt(df.cst, df.flow)

print(df)
print(df.describe())
