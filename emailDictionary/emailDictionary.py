fname = input('Enter file: ')

try:
    fhandle = open(fname)
except:
    print('File not found. Check file name.')

d = dict()
e = []
for line in fhandle:
    if not line.startswith('From '): continue
    words = line.split()
    e.append(words[1])

for x in e:
    d[x] = d.get(x, 0) + 1

maxC = None
maxE = None
for k,v in d.items():
    if maxC is None or v > maxC:
        maxE = k
        maxC = v

print(maxE, maxC)
