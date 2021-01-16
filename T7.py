def greet(lang): #you can create a function without adding any term inside '()'
    if lang=='es': #the 'es' 'ma' 'en' etc. are what is known as arguments
        return 'Hola'
    elif lang=='ma':
        return 'Enthada panni'
    elif lang=='tn':
        return 'Enthirr pedkane thambi'
    elif lang=='fr':
        return 'bonjour'
    elif lang=='en':
        return 'Tf you want? '
    else:
        print('Enter a valid lang u biyatch')
y=input('Enter your name ')
x=input('Enter language.. eg:ma,en,tn.. \n')
print(greet(x),y) #invoking or calling the function
#simple calling is like >>greet()  and thats it.
#here the function is with parameters
