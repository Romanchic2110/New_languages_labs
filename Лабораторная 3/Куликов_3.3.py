import sys

for line in sys.stdin:
    s = line.rstrip('\n')
    if s.strip().startswith('#') and not s.strip().startswith('#!'):
        continue
    print(s)