n=5
while n>0:
    print(n)
    n=n-1
print('Blastoff!')
print(n)

for i in [5,4,3,2,1]:
    print(i)
print('Blastoff!')
    
while True:
    #provide any true condition.. 'True' basically gives an infinite loop
    line=input('>')
    if line=='done':
        break
    print(line)
print('Done!')
 #if we use 'continue' it won't exit the loop like break it will exit out of-
 #the current looping (i.e, next iteration)
