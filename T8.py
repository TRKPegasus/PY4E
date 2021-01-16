hours=input('Enter the hours: ')
hours=float(hours)
rate=input('Enter the rate: ')
rate=float(rate)
def computepay():
    if hours<=40:
        pay=hours*rate
    else:
        ot=(hours-40)*(rate*0.5)
        pay=hours*rate
        pay=pay+ot
    return pay
print('Pay',computepay())
