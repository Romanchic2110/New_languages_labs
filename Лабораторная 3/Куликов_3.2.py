import sys

count = 0
for line in sys.stdin:
    s = line.strip()
    if s.startswith('#') and not s.startswith('#!'):
        count += 1
print(count)