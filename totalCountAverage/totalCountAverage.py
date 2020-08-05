count = 0
total = 0.0

while True:
    snum = input('Enter a number:')
    if snum == 'done' :
        break
    try:
        fnum = float(snum)
    except:
        print('Invalid input')
        continue
    count += 1
    total = total + fnum

a = total/count
print (f'Total is {total}. Count is {count}. Average is {a}.')
