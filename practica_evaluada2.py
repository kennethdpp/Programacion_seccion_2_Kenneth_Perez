numero=int(input('ingrese una calificacion: '))
if numero<0:
    print('calificacion invalida')
elif numero==100:
    print('calificacion perfecta')
elif numero>=90 and numero<100:
    print('excelente')
elif numero>=70 and numero<90:
    print('bueno')
elif numero>=50 and numero<70:
    print('suficiente')
elif numero<50:
    print('insuficiente')
else:
    print('calificacion invalida')