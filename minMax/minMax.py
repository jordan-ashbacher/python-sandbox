largest = None
smallest = None

while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    try:
        i = int(num)
    except:
        print('Invalid input')
        continue

    if largest is None or largest < i:
        largest = i

    if smallest is None or smallest > i:
        smallest = i
        
print('Maximum is', largest)
print('Minimum is', smallest)
