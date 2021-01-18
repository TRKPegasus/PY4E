largest = 'none'
smallest = 'none'
while True:
    x=input('Enter a number: ')
    if x=='done':
        print('Maximum is',largest)
        print('Minimum is',smallest)
        break
    try:
        x=int(x)
    except:
        print('Invalid input')
        continue
    if largest == 'none':
        largest=x
    elif largest<x:
        largest=x
    if smallest == 'none':
        smallest=x
    elif smallest>x:
        smallest=x
