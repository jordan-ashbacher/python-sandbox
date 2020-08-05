fname = input('Enter file name: ')
count = 0
total = 0

try:
    fhandle = open(fname)
except:
    print('File not found. Please check the file name.')

for line in fhandle:
    if not line.startswith('X-DSPAM-Confidence:'): continue
    if line.startswith('X-DSPAM-Confidence:'):
        count += 1
        lx = line.rstrip()
        ly = lx.find(" ")
        lf = float(lx[ly:])
        total = total + lf

average = total/count
print('Average spam confidence:', average)
