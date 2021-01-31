import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mysql.connector
import sys
from datetime import datetime, timedelta

pe = pd.read_sql_query("select * from pulpeye where SampleTime > '2020-11-21 00:00:00' ", local_db)


# Get current time and arguments
now = datetime.now()
last_sample_time = pe.SampleTime.max()
now = last_sample_time

current_time = now.strftime("%Y-%m-%d %H:%M:%S")
print("Current Time =", current_time)
print ('Number of arguments: {} arguments'.format(len(sys.argv)))

print('Last sample {}'.format(pe.SampleTime.max()))

hours_back = 24   # default period to look back

if len(sys.argv) > 1:
  if sys.argv[1] == 'w':
    sys.argv[1] = 168
  if sys.argv[1] == 'm':
    sys.argv[1] = 672
  if sys.argv[1] == '2d':
    sys.argv[1] = 48    
  if sys.argv[1] == 'q':
    sys.argv[1] = 2016  
  hours_back = int(sys.argv[1])
  # one letter code options

# Determine start and end times for data
start_time_dt = now - timedelta(hours = hours_back)
start_time = start_time_dt.strftime("%Y-%m-%d %H:%M:%S")
end_time = current_time

if len(sys.argv) > 2:
  hours_back = int(sys.argv[1])
  end_hours_back = int(sys.argv[2])
  end_time_dt = now - timedelta(hours = end_hours_back)
  end_time = end_time_dt.strftime("%Y-%m-%d %H:%M:%S")

# Filter data to period   hours back to start...  hours back to end
pe = pe[pe.SampleTime > start_time]
pe = pe[pe.SampleTime < end_time]

# data separated by sample point
pe_mc6 = pe[pe.PulpName == 'MC6']
pe_mc1 = pe[pe.PulpName == 'MC1']
pe_rej = pe[pe.PulpName == 'Ref_Rejects']
pe_l1 = pe[pe.PulpName == 'L1_Lat_Transfer']
pe_l3 = pe[pe.PulpName == 'L3_Lat_Transfer']
pe_l2 = pe[pe.PulpName == 'L2_Lat_Transfer']

# Create plot figure and axis
fig = plt.figure('TMP Quality Window', figsize=(10, 6))
ax = fig.add_subplot(1,1,1)

fig.suptitle('Look back {} hours'.format(hours_back))
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }

plt.style.use('seaborn-dark-palette')
plt.scatter(x=pe_mc6.CSF, y=pe_mc6.FL, s=9, c='black', marker='o')
plt.scatter(x=pe_mc1.CSF, y=pe_mc1.FL, s=9, c='g', marker='D', alpha = 0.55)
plt.scatter(x=pe_rej.CSF, y=pe_rej.FL, s=9, c='m', marker='s')
plt.scatter(x=pe_l1.CSF, y=pe_l1.FL, s=11, c='b', marker='v')
plt.scatter(x=pe_l3.CSF, y=pe_l3.FL, s=11, c='r', marker='^')
plt.scatter(x=pe_l2.CSF, y=pe_l2.FL, s=11, c='g', marker='>')

plt.axvline(pe_mc6.CSF.mean(), color = 'black', ls = '--')
plt.axvline(pe_mc1.CSF.mean(), color = 'g', ls = '--')
plt.axvline(pe_rej.CSF.mean(), label = 'Rejects Avg', color = 'm', ls = '--')
plt.axvline(pe_l1.CSF.mean(), label = 'L1 Avg', color = 'b', ls = '--')
plt.axvline(pe_l2.CSF.mean(), label = 'L2 Avg', color = 'g', ls = '--')
plt.axvline(pe_l3.CSF.mean(), label = 'L3 Avg', color = 'r', ls = '--')

plt.axhline(pe_mc6.FL.mean(), color = 'black', ls = '--')
plt.axhline(pe_mc1.FL.mean(), color = 'g', ls = '--')
plt.axhline(pe_rej.FL.mean(), label = 'Rejects Avg', color = 'm', ls = '--')
plt.axhline(pe_l1.FL.mean(), label = 'L1 Avg', color = 'b', ls = '--')
plt.axhline(pe_l2.FL.mean(), label = 'L2 Avg', color = 'g', ls = '--')
plt.axhline(pe_l3.FL.mean(), label = 'L3 Avg', color = 'r', ls = '--')


plt.title('Quality Window\n' + start_time + ' --  ' + end_time, fontdict=font, loc='left')
plt.legend(['MC6', 'MC1', 'Rejects', 'L1', 'L2', 'L3'])

font['size'] = 12
plt.xlabel('Freeness (ml)', fontdict=font)
plt.ylabel('Fibre Lenth (mm)', fontdict=font)
majorx_ticks = np.arange(40, 250, 10)
ax.set_xticks(majorx_ticks)
majory_ticks = np.arange(1.4, 2, 0.05)
ax.set_yticks(majory_ticks)
plt.grid(which='both', linestyle='--', linewidth=1)

plt.xlim(40, 250)
plt.ylim(1.4, 1.95)

day_of_year = datetime.now().timetuple().tm_yday + 365
# print('{}: {}'.format(day_of_year, shift_list[day_of_year-1]))
# print('Day of year: {}   Day Shift: {}'.format(pe.doy, pe.day_shift))

print(pe_mc6.corr())

print(pe_rej.tail())
plt.savefig('qw_now.png', dpi=600)
plt.show()
