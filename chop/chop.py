def chop(x):
    del x[0]
    del x[-1]
    return x

numlist = [5, 6, 7, 8, 9]
y = chop(numlist)
print(y)
