import os 
import time 

contador2=3 
contador=1

os.system('cls')
#totales
totalsushi1=0
totalsushi2=0
totalsushi3=0
totalsushi4=0
#platas
platasushi1=0
platasushi2=0
platasushi3=0
platasushi4=0
#codigo
codigo='soyotaku'

while contador2==3:
    print(' RESTAURANTE DELIVERY LUIS SUSHI ****AL TERMINAR EL PEDIDO PUEDE APLICAR CODIGO DE DESCUENTO********** ') 
    print(' a continuacion sus datos')
    nombre=input(' Nombre:      ')
    direccion=input(' Direccion (Nombre Calle) :    ')
    numerodireccion=input( ' Numero Casa/Departamento :      ')
    time.sleep(2)
    contador2=1
    



os.system('cls')

while contador >0:
    print()
    print(''' BIENVENIDO AL MENU DE NUESTRO RESTAURANTE DELIVERY LUIS SUSHI's 
          
            *COMPRAR*
          
            1. Pikachu Roll $4500
            2. Otaku Roll $5000
            3. Pulpo Venenoso Roll $5200
            4. Anguila Eléctrica Roll $4800   

            *** SEGUNDAS OPCIONES *****
             
            5. Mostrar Pedido
            6. Salir
            
                                     ''')
    try:
        opc=int(input(' LUIS SUSHI ELECCION 1-6 '))
    except ValueError:
        print(' opcion equivocada')
        continue

    if opc==1:
        print()
        cuantossushi1=int(input( ' Cuantos Pikachu Roll Desea ? :       '))
        print()
        platasushi1+=(cuantossushi1*4500)
        totalsushi1+=cuantossushi1
        ###############
        res=input(''' DESEA VOLVER AL MENU  ?   
                   Escribir ----> si/no  --->:        ''')
        if res=='si':
            contador=1
        #####################
        elif res=='no':
            os.system('cls')
            tienecodigo=input(''' TIENE CODIGO DE DESCUENTO ? 
                                    ESCRIBIR ''si'' o ''no'' 
                                    ''')
            
            if tienecodigo=='si':
                pruebacodigo=input(''' ESCRIBA EL CODIGO 
                                       PARA IR AL MENU LETRA X ''')
                
                if pruebacodigo=='soyotaku':
                    print(' codigo aceptado ')
                    print(f'''****************************
                    Muchas gracias {nombre}
                    Total Productos = {totalsushi1+totalsushi2+totalsushi3+totalsushi4}
                    ******************************
                    Pikachu Roll : {totalsushi1} 
                    Otaku Roll :   {totalsushi2}
                    Pulpo venenoso Roll: {totalsushi3}
                    Anguila Electrica Roll :  {totalsushi4}            
                    ********************
                    Subtotal por pagar: {platasushi1+platasushi2+platasushi3+platasushi4}
                    Descuento por codigo: 10 % 
                    TOTAL: {(platasushi1+platasushi2+platasushi3+platasushi4)*0.9}                     

                                                 ''')
                    contador=0
                elif pruebacodigo=='x':
                    contador=1
                else:
                    print(' opcion equivocada')
                    print(' VOLVERA AUTOMATICAMENTE AL MENU ')
                    time.sleep(2)
                
            elif tienecodigo=='no':
                print(' no tienes descuento')
                print(f'''****************************
                    Muchas gracias {nombre}
                    Total Productos = {totalsushi1+totalsushi2+totalsushi3+totalsushi4}
                    ******************************
                    Pikachu Roll : {totalsushi1} 
                    Otaku Roll :   {totalsushi2}
                    Pulpo venenoso Roll: {totalsushi3}
                    Anguila Electrica Roll :  {totalsushi4}            
                    ********************
                    Subtotal por pagar: {platasushi1+platasushi2+platasushi3+platasushi4}
                    Descuento por codigo: 0
                    TOTAL: {platasushi1+platasushi2+platasushi3+platasushi4} ''')
                contador=0
            else:
                print('opcion equivocada')
                
        else:
            print(' opcion equivocada')




    elif opc==2:
        cuantossushi2=int(input( ' Cuantos Otaku Roll Desea ? :       '))
        totalsushi2+=cuantossushi2
        platasushi2+=(cuantossushi2*5000)
        ##
        res=input(''' DESEA VOLVER AL MENU  ?   
                   Escribir ----> si/no  --->:        ''')
        if res=='si':
            contador=1
        #####################
        elif res=='no':
            os.system('cls')
            tienecodigo=input(''' TIENE CODIGO DE DESCUENTO ? 
                                    ESCRIBIR ''si'' o ''no'' 
                                    ''')
            
            if tienecodigo=='si':
                pruebacodigo=input(''' ESCRIBA EL CODIGO 
                                       PARA IR AL MENU LETRA X ''')
                
                if pruebacodigo=='soyotaku':
                    print(' codigo aceptado ')
                    print(f'''****************************
                    Muchas gracias {nombre}
                    Total Productos = {totalsushi1+totalsushi2+totalsushi3+totalsushi4}
                    ******************************
                    Pikachu Roll : {totalsushi1} 
                    Otaku Roll :   {totalsushi2}
                    Pulpo venenoso Roll: {totalsushi3}
                    Anguila Electrica Roll :  {totalsushi4}            
                    ********************
                    Subtotal por pagar: {platasushi1+platasushi2+platasushi3+platasushi4}
                    Descuento por codigo: 10 % 
                    TOTAL: {(platasushi1+platasushi2+platasushi3+platasushi4)*0.9}                     

                                                 ''')
                    contador=0
                elif pruebacodigo=='x':
                    contador=1
                else:
                    print(' opcion equivocada')
                    print(' VOLVERA AUTOMATICAMENTE AL MENU ')
                    time.sleep(2)
                
            elif tienecodigo=='no':
                print(' no tienes descuento')
                print(f'''****************************
                    Muchas gracias {nombre}
                    Total Productos = {totalsushi1+totalsushi2+totalsushi3+totalsushi4}
                    ******************************
                    Pikachu Roll : {totalsushi1} 
                    Otaku Roll :   {totalsushi2}
                    Pulpo venenoso Roll: {totalsushi3}
                    Anguila Electrica Roll :  {totalsushi4}            
                    ********************
                    Subtotal por pagar: {platasushi1+platasushi2+platasushi3+platasushi4}
                    Descuento por codigo: 0
                    TOTAL: {platasushi1+platasushi2+platasushi3+platasushi4} ''')
                contador=0
            else:
                print('opcion equivocada')
        else:
            print(' opcion equivocada')



    elif opc==3:
        cuantossushi3=int(input( ' Cuantos Pulpo Venenoso Roll Desea ? :       '))
        totalsushi3+=cuantossushi3
        platasushi3+=(cuantossushi3*5200)

        #####3
        res=input(''' DESEA VOLVER AL MENU  ?   
                   Escribir ----> si/no  --->:        ''')
        if res=='si':
            contador=1
        #####################
        elif res=='no':
            os.system('cls')
            tienecodigo=input(''' TIENE CODIGO DE DESCUENTO ? 
                                    ESCRIBIR ''si'' o ''no'' 
                                    ''')
            
            if tienecodigo=='si':
                pruebacodigo=input(''' ESCRIBA EL CODIGO 
                                       PARA IR AL MENU LETRA X ''')
                
                if pruebacodigo=='soyotaku':
                    print(' codigo aceptado ')
                    print(f'''****************************
                    Muchas gracias {nombre}
                    Total Productos = {totalsushi1+totalsushi2+totalsushi3+totalsushi4}
                    ******************************
                    Pikachu Roll : {totalsushi1} 
                    Otaku Roll :   {totalsushi2}
                    Pulpo venenoso Roll: {totalsushi3}
                    Anguila Electrica Roll :  {totalsushi4}            
                    ********************
                    Subtotal por pagar: {platasushi1+platasushi2+platasushi3+platasushi4}
                    Descuento por codigo: 10 % 
                    TOTAL: {(platasushi1+platasushi2+platasushi3+platasushi4)*0.9}                     

                                                 ''')
                    contador=0
                elif pruebacodigo=='x':
                    contador=1
                else:
                    print(' opcion equivocada')
                    print(' VOLVERA AUTOMATICAMENTE AL MENU ')
                    time.sleep(2)
                
            elif tienecodigo=='no':
                print(' no tienes descuento')
                print(f'''****************************
                    Muchas gracias {nombre}
                    Total Productos = {totalsushi1+totalsushi2+totalsushi3+totalsushi4}
                    ******************************
                    Pikachu Roll : {totalsushi1} 
                    Otaku Roll :   {totalsushi2}
                    Pulpo venenoso Roll: {totalsushi3}
                    Anguila Electrica Roll :  {totalsushi4}            
                    ********************
                    Subtotal por pagar: {platasushi1+platasushi2+platasushi3+platasushi4}
                    Descuento por codigo: 0
                    TOTAL: {platasushi1+platasushi2+platasushi3+platasushi4} ''')
                contador=0
            else:
                print('opcion equivocada')
        else:
            print(' opcion equivocada')




    elif opc==4:
        cuantossushi4=int(input( ' Cuantos Anguila Eléctrica Roll Desea ? :       '))
        totalsushi4+=cuantossushi4
        platasushi4+=(cuantossushi4*4800)

        ####3
        res=input(''' DESEA VOLVER AL MENU  ?   
                   Escribir ----> si/no  --->:        ''')
        if res=='si':
            contador=1
        #####################
        elif res=='no':
            os.system('cls')
            tienecodigo=input(''' TIENE CODIGO DE DESCUENTO ? 
                                    ESCRIBIR ''si'' o ''no'' 
                                    ''')
            
            if tienecodigo=='si':
                pruebacodigo=input(''' ESCRIBA EL CODIGO 
                                       PARA IR AL MENU LETRA X ''')
                
                if pruebacodigo=='soyotaku':
                    print(' codigo aceptado ')
                    print(f'''****************************
                    Muchas gracias {nombre}
                    Total Productos = {totalsushi1+totalsushi2+totalsushi3+totalsushi4}
                    ******************************
                    Pikachu Roll : {totalsushi1} 
                    Otaku Roll :   {totalsushi2}
                    Pulpo venenoso Roll: {totalsushi3}
                    Anguila Electrica Roll :  {totalsushi4}            
                    ********************
                    Subtotal por pagar: {platasushi1+platasushi2+platasushi3+platasushi4}
                    Descuento por codigo: 10 % 
                    TOTAL: {(platasushi1+platasushi2+platasushi3+platasushi4)*0.9}                     

                                                 ''')
                    contador=0
                elif pruebacodigo=='x':
                    contador=1
                else:
                    print(' opcion equivocada')
                    print(' VOLVERA AUTOMATICAMENTE AL MENU ')
                    time.sleep(2)
                
            elif tienecodigo=='no':
                print(' no tienes descuento')
                print(f'''****************************
                    Muchas gracias {nombre}
                    Total Productos = {totalsushi1+totalsushi2+totalsushi3+totalsushi4}
                    ******************************
                    Pikachu Roll : {totalsushi1} 
                    Otaku Roll :   {totalsushi2}
                    Pulpo venenoso Roll: {totalsushi3}
                    Anguila Electrica Roll :  {totalsushi4}            
                    ********************
                    Subtotal por pagar: {platasushi1+platasushi2+platasushi3+platasushi4}
                    Descuento por codigo: 0
                    TOTAL: {platasushi1+platasushi2+platasushi3+platasushi4} ''')
                contador=0
            else:
                print('opcion equivocada')
        else:
            print(' opcion equivocada')



    elif opc==5:
        os.system('cls')
        print(f'''  *** PEDIDO ***
              
                Pikachu Roll : {totalsushi1}
                Otaku Roll :    {totalsushi2}
                Pulpo venenoso Roll: {totalsushi3}
                Anguila Electrica Roll : {totalsushi4   } ''')
        print()
        res=input(''' DESEA VOLVER AL MENU  ?   
                   Escribir ----> si/no  --->:        ''')
        if res=='si':
            contador=1
        #####################
        elif res=='no':
            os.system('cls')
            tienecodigo=input(''' TIENE CODIGO DE DESCUENTO ? 
                                    ESCRIBIR ''si'' o ''no'' 
                                    ''')
            
            if tienecodigo=='si':
                pruebacodigo=input(''' ESCRIBA EL CODIGO 
                                       PARA IR AL MENU LETRA X ''')
                
                if pruebacodigo=='soyotaku':
                    print(' codigo aceptado ')
                    print(f'''****************************
                    Muchas gracias {nombre}
                    Total Productos = {totalsushi1+totalsushi2+totalsushi3+totalsushi4}
                    ******************************
                    Pikachu Roll : {totalsushi1} 
                    Otaku Roll :   {totalsushi2}
                    Pulpo venenoso Roll: {totalsushi3}
                    Anguila Electrica Roll :  {totalsushi4}            
                    ********************
                    Subtotal por pagar: {platasushi1+platasushi2+platasushi3+platasushi4}
                    Descuento por codigo: 10 % 
                    TOTAL: {(platasushi1+platasushi2+platasushi3+platasushi4)*0.9}                     

                                                 ''')
                    contador=0
                elif pruebacodigo=='x':
                    contador=1
                else:
                    print(' opcion equivocada')
                
            elif tienecodigo=='no':
                print(' no tienes descuento')
                print(f'''****************************
                    Muchas gracias {nombre}
                    Total Productos = {totalsushi1+totalsushi2+totalsushi3+totalsushi4}
                    ******************************
                    Pikachu Roll : {totalsushi1} 
                    Otaku Roll :   {totalsushi2}
                    Pulpo venenoso Roll: {totalsushi3}
                    Anguila Electrica Roll :  {totalsushi4}            
                    ********************
                    Subtotal por pagar: {platasushi1+platasushi2+platasushi3+platasushi4}
                    Descuento por codigo: 0
                    TOTAL: {platasushi1+platasushi2+platasushi3+platasushi4} ''')
                contador=0
            else:
                print('opcion equivocada')
        else:
            print(' opcion equivocada')





    elif opc==6:
        print(f' MUCHAS GRACIAS POR ESTAR CON NOSOTROS {nombre} , TU PEDIDO LLEGARA ENTRE 0-30 MINUTOS a {direccion} numero: {numerodireccion}')
        contador=0


    else:
        print('opcion equivocada')
    


    