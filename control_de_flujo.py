
"""Guarde en lista `naturales` los primeros 100 números naturales (desde el 1) 
usando el bucle while
"""

naturales=[]
i= 1
while i<=100:
 naturales.append(i)
 i+=1
 #continue
#print(naturales)

"""Guarde en `acumulado` una lista con el siguiente patrón:

['1','1 2','1 2 3','1 2 3 4','1 2 3 4 5',...,'...47 48 49 50']

Hasta el número 50.
"""

#naturales50=[]
ii= 1
acumulado=[]
cadena1=''
while ii<=50:
 jj=ii
 
 #while jj<50:
 
 cadena1=  cadena1+' '+str(ii)
 cadena1=cadena1.strip()
 acumulado.append(cadena1)
 ii=ii+1
#print('acumulado: ',acumulado)
 
#print('valor cadena1:',cadena1, ii, jj)
 # jj+=1
  #print(cadena1)
 

#print ("acumulado", acumulado, '\n')
#cincuenta=''
#cincuenta= naturales(range (0,50,1))


#print(list(range(0,50,1))



"""Guarde en `suma100` el entero de la suma de todos los números entre 1 y 100:
"""


suma100=0

for numero in naturales:
 suma100=numero+suma100 
 #print(numero)
#print(suma100) 


"""Guarde en `tabla100` un string con los primeros 10 múltiplos del número 134, 
separados por coma, así:

'134,268,...'

"""
a=1
b=134
zz=0
#zz=''
qq=''
tabla1000=''
ltabla100=[]

for zz in range(1,11):
     a=zz*b
     
     tabla1000=tabla1000+','+str(a)
     tabla100=str(tabla1000[1:])
      

print("tabla100:",tabla100) 
#print(ltabla100)

#istaUnida=  listaUnida + str(self.lista[x])
 #       listaUnida=','.join(listaUnida)


"""Guardar en `multiplos3` la cantidad de números que son múltiplos de 3 y 
menores a 300 en la lista `lista1` que se define a continuación (la lista 
está ordenada).
"""
lista1 = [12, 15, 20, 27, 32, 39, 42, 48, 55, 66, 75, 82, 89, 91, 93, 105, 123, 132, 150, 180, 201, 203, 231, 250, 260, 267, 300, 304, 310, 312, 321, 326]

lista=[numero for numero in lista1 if numero % 3==0 and numero <300]
multiplos3=len(lista)
#print("cantidad de numeros: ", multiplos3)



"""Guardar en `regresivo50` una lista con la cuenta regresiva desde el número 
50 hasta el 1, así:

[
  '50 49 48 47...',
  '49 48 47 46...',
  ...
  '5 4 3 2 1',
  '4 3 2 1',
  '3 2 1',
  '2 1',
  '1'
]
"""



naturales50=[]
i= 50
regresivo50=[]

while i>0:
 j=i
 cadena=''
 while j>0:
  cadena= cadena + ' ' + str(j)
  j-=1
 i-=1
 cadena=cadena.strip()
 regresivo50.append(cadena)
#print ("regresivos50:",regresivo50, '\n')
#range(50, 0, -1)



#regresivo50=list(reversed((naturales50)))# esto no se debe hacer es ineficiente
#print('regresivo', regresivo50)


"""Invierta la siguiente lista usando el bucle for y guarde el resultado en 
`invertido` (sin hacer uso de la función `reversed` ni del método `reverse`)
"""
lista2 = list(range(1, 70, 5))
print('lista2',lista2)
invertido=[]
#aa=0
print ('len ', len(lista2))
for aa in range((len(lista2)-1),-1,  -1):
    print('elemento lista',lista2[aa] )
    invertido.append(lista2[aa])
    print('aca voy:', invertido)
print('invertido: ', invertido)



"""Guardar en `primos` una lista con todos los números primos desde el 37 al 300
Nota: Un número primo es un número entero que no se puede calcular multiplicando 
otros números enteros.
"""


aux=0
c=0
x=0
suma=0
primos=[]

num=37


while num<=300:

 aux=1

 c=0

 while aux<=num:

  if num%aux==0:

   c=c+1

  
  aux=aux+1

 

 if c==2 :
  primos.append(num)
  x=x+1

  suma=suma+num
  
 
 

 num=num+1



#print( "Hay ",x," Numeros Primos")

#print( "Sumatoria ",suma)
#print("primos: ", primos)



"""Guardar en `fibonacci` una lista con los primeros 60 términos de la serie de 
Fibonacci.
Nota: En la serie de Fibonacci, los 2 primeros términos son 0 y 1, y a partir 
del segundo cada uno se calcula sumando los dos anteriores términos de la serie.

[0, 1, 1, 2, 3, 5, 8, ...]

"""
fibonacci= [0,1]

for i in range(2, 60):
  fibonacci.append(fibonacci[-1] + fibonacci[-2])
#print(fibonacci)






"""Guardar en `factorial` el factorial de 30
El factorial (símbolo:!) Significa multiplicar todos los números enteros desde
el 1 hasta el número elegido.

Por ejemplo, el factorial de 5 se calcula así:

5! = 5 × 4 × 3 × 2 × 1 = 120
"""

factorial=1
n=30
for i in range(1,n+1):
  factorial=factorial*i
#print('factorial: ', factorial )



"""Guarde en lista `pares` los elementos de la siguiente lista que esten 
presentes en posiciones pares, pero solo hasta la posición 80.
"""

lista3 = [941, 149, 672, 208, 99, 562, 749, 947, 251, 750, 889, 596, 836, 742, 512, 19, 674, 142, 272, 773, 859, 598, 898, 930, 119, 107, 798, 447, 348, 402, 33, 678, 460, 144, 168, 290, 929, 254, 233, 563, 48, 249, 890, 871, 484, 265, 831, 694, 366, 499, 271, 123, 870, 986, 449, 894, 347, 346, 519, 969, 242, 57, 985, 250, 490, 93, 999, 373, 355, 466, 416, 937, 214, 707, 834, 126, 698, 268, 217, 406, 334, 285, 429, 130, 393, 396, 936, 572, 688, 765, 404, 970, 159, 98, 545, 412, 629, 361, 70, 602]



pares=[]
#pares=[paro for paro in lista3 if paro%2==0 and paro <80]
#pares.append(lista3)
#print('numero par', pares) 


#lista=[numero for numero in lista1 if numero % 3==0 and numero <300]
#multiplos3=len(lista)

for cc in range (0,81, 1):
    print(lista3)
    if cc%2==0:
        pares.append(lista3[cc])
        print('posicion', cc, 'elemento', lista3[cc])
print('la lista con posisciones pares', pares) 






"""Guarde en lista `cubos` el cubo (potencia elevada a la 3) de los números del 
1 al 100. 
"""
cubos=[]
potencia3=0

for numero in naturales:
 potencia3=numero**3
 cubos.append(potencia3)
 #print(potencia3) 



"""Encuentre la suma de la serie 2 +22 + 222 + 2222 + .. hasta sumar 10 términos 
y guardar resultado en variable `suma_2s` 
"""
y= 0

for i in range(0, 11):
    t = 10 ** i * (10 - i) * 2
    y = t + y
suma_2s = y
#print(suma_2s)






"""Guardar en un string llamado `patron` el siguiente patrón llegando a una 
cantidad máxima de asteriscos de 30. 
*
**
***
****
*****
******
*******
********
*********
********
*******
******
*****
****
***
**
*
"""



ast = '*\n'
c = '******************************\n'
y = '*'
for a in range(2, 30):
  y= '*'
  y = y * a
  ast = ast + y + '\n'
print(ast)

for a in range(29, 0, -1):
  y = '*'
  y = y * a
  c = c + y + '\n'
print(c)

patron = ast + c
patron = patron[:-1]
print(patron)
