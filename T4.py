#Put in the dangerous possible error invoking code in try and try no.2 in except. It wont return traceback if try no.1 is a bad code.
x=input()
try:
    x=x+1
    print(x)
except:
    x=int(x)
    x=x+1
    print(x)
