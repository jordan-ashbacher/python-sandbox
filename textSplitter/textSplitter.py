fname = input('Enter file name: ')

try:
    fhandle = open(fname)
except:
    print('Please check the file name')

lst = list()

for line in fhandle:
    words = line.split()
    for word in words:
        if word in lst : continue
        lst.append(word)
        lst.sort()

print(lst)
