while True:
    a=int(input('enter the integer '))
    if a==0:
        print('number of digits = 1')
    else:
        t=0
        while(a!=0):
            t+=1
            a=int(a/10)
        print('number of digits = ',t)
            
    
