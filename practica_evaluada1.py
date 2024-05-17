numero=int(input('ingrese un numero entero: '))
if numero%2==0:
    print('el numero es divisible por dos')
elif numero>100:
    print('el numero es mayor que 100')
elif numero%3==0:
    print('el numero es divisible por tres')
elif numero<0:
    print('el numero es negativo')
elif numero%2==0 and numero%3==0:
    print('el numero es divisible por seis')
else:
    print('el numero no cumple ninguna condicion especial')