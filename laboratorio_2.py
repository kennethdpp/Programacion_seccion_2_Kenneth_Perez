N=input('ingrese la cantidad de numeros primos que desee, esbriba "stop" para dejar de emular numeros: ')
L=0
while N!='stop':
    while not N.isnumeric():
        print('no es un valor numerico, intente de nuevo')
        N=input('ingrese un numero primo: ')
        es_primo=True
        for i in range(2,N):
            if N%i==0:
                es_primo=False
                N=input('no es un numero primo, inrese un numero primo: ')
    K=int(N)
    C=K*K
    break
L=L+C
print(L)
