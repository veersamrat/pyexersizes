def fibonacci(n):
    if n==0 or n==1:
        # print('0')
        return n
    else:
        #print(fibonacci(n-1)+fibonacci(n-2))
        return fibonacci(n-1)+fibonacci(n-2)

noflevel=9

for i in range(noflevel):
       print(fibonacci(i))