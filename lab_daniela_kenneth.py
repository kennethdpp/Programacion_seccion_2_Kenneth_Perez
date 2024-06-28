user_text=input('quiere codificar o decodificar?: ').lower()
abc='abcdefghijklmnñopqrstuvwxyz'
abc_total=''
if user_text=='codificar':
    user_cod=input('codificacion por "cesar" o por "primos"?: ').lower()
    if user_cod=='cesar':
        abc_inicial=abc[:len(abc)-7]
        abc_final=abc[len(abc)-7:]
        abc_total=abc_final+abc_inicial
        
        dict_1={}
        for i in range(len(abc)):
            dict_1[abc[i]]=abc_total[i]
            
        palabra_1=input('escriba para codificar: ').lower()
        palabra_1_lista=list(palabra_1)
        palabra_cifrada_1=''
        
        for letra_1 in palabra_1_lista:
            palabra_cifrada_1+=dict_1[letra_1]
        print(palabra_cifrada_1)
        
    elif user_cod=='primos':
        prm=[]
        numero=1
        while numero<=104:
            contador_1=1
            contador_2=0
            while contador_1<=numero:
                if numero%contador_1==0:
                    contador_2+=1
                contador_1+=1
            if contador_2==2:
                prm.append(str(numero))
            numero+=1
            
        dict_2={}
        for i in range(len(abc)):
            dict_2[abc[i]]=prm[i]
        
        palabra_2=input('escribe para codificar: ').lower()
        palabra_2_lista=list(palabra_2)
        palabra_cifrada_2=''
        
        for letra_2 in palabra_2_lista:
            palabra_cifrada_2+=dict_2[letra_2]+'-'
        print(palabra_cifrada_2)
        
elif user_text=='decodificar':
    user_cod=input('decodificacion por "cesar" o por "primos"?: ').lower()
    if user_cod=='cesar':
        abc_inicial=abc[:len(abc)-7]
        abc_final=abc[len(abc)-7:]
        abc_total=abc_final+abc_inicial
        
        dict_3={}
        for k in range(len(abc)):
            dict_3[abc_total[k]]=abc[k]
            
        palabra_3=input('escriba para decodificar: ').lower()
        palabra_3_lista=list(palabra_3)
        palabra_descifrada_1=''
        
        for letra_3 in palabra_3_lista:
            palabra_descifrada_1+=dict_3[letra_3]
        print(palabra_descifrada_1)
    elif user_cod=='primos':
        prm=[]
        numero=1
        while numero<=104:
            contador_1=1
            contador_2=0
            while contador_1<=numero:
                if numero%contador_1==0:
                    contador_2+=1
                contador_1+=1
            if contador_2==2:
                prm.append(numero)
            numero+=1
            
        dict_4={}
        for l in range(len(abc)):
            dict_4[prm[l]]=abc[l]
        
        palabra_4=(input('escribe los numeros para decodificar, escriba "stop" para dejar de escribir numeros: '))
        palabra_4_lista=[]
        while palabra_4:
            if palabra_4=='stop':
                break
            else:
                palabra_4_lista.append(int(palabra_4))
                palabra_4=(input('ingrese otro numero: '))
                
        palabra_descifrada_2=''
        
        for letra_4 in palabra_4_lista:
            palabra_descifrada_2=palabra_descifrada_2+dict_4[letra_4]
        print((palabra_descifrada_2))  
        