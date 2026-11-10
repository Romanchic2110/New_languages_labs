import sys
from datetime import datetime

dates = [datetime.strptime(line.strip(), '%d.%m.%Y') for line in sys.stdin if line.strip()]

asc = all(dates[i] < dates[i + 1] for i in range(len(dates) - 1))
desc = all(dates[i] > dates[i + 1] for i in range(len(dates) - 1))

if asc: print('ASC')
elif desc: print('DESC')
else: print('MIX')