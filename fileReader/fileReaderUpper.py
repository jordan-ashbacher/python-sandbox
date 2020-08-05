fname = input('Enter file name: ')
fhand = open(fname)

for line in fhand:
    ly = line.rstrip()
    print(ly.upper())
