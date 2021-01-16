x=input('Enter the score: ')
try:
    x=float(x)
except:
    print('Enter a numeric value..')
    quit()
if (x<1.0) and (x>0.0):
    if x>=0.9:
        print('A')
    elif x>=0.8:
        print('B')
    elif x>=0.7:
        print('C')
    elif x>=0.6:
        print('D')
    else:
        print('F')
else:
    print('Enter a valid score..')
