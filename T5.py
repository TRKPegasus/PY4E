#pay per hour and overtime rate of 1.5 times per overtime hours
x=input('Enter the hours: ')
y=input('Enter the rate per hour: ')
try:
    x=float(x)
    y=float(y)
except:
    print('Enter a numeric input..')
    quit()    # you can use exit() also.
if x<=40:
    pay=(x*y)
else:
    pay=(x*y)
    ot=(x-40)*(y*0.5)
    pay=pay+ot
print(pay)
