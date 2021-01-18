a=-1 #or just add 'None'(which just a word no signi beyond that) value.
print('Before', a)
for i in [12,34,56,78,43,2,21,344,335,678,245,78.69.32]:
    #when using 'none' value add
    #if a is None:
    #   a=value
    #instead of if add elif below
    if i>a:     #i<a for smallest with 'a' contaning 'none' value
        a=i
    print(a,i)
print('After',a)
#use largest_so_far(smallest_so_far) instead of 'a' for ease
count=0
sum=0
print('Before', count, sum)
for value in [12,23,43,1,234,442,23,439,57,69]:
    count=count+1
    sum=sum+value
    print(count, value, sum)
print('After', count, sum, 'Average=' sum/count)
