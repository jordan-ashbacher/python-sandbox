fname = input('Enter file name: ')

try:
    fhandle = open(fname)
except:
    print('File not found.')
d = dict()
lst = []
for line in fhandle:
    if not line.startswith('From '): continue
    words = line.split()
    time = words[5]
    hour = time.split(':')
    lst.append(hour[0])

for h in lst:
    d[h] = d.get(h,0) + 1

r = (sorted([(k,v) for k,v in d.items()]))

for k,v in r:
    print(k, v)
