fname = input('Enter file name: ')

try:
    fhandle = open(fname)
except:
    print('File not found. Check file name.')

count = 0

for line in fhandle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    count += 1
    words = line.split()
    print(words[1])

print("There were", count, "lines in the file with From as the first word")
