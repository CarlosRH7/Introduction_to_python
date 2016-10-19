# lista =[10,5,2,7,9]
# total = len(lista)
# i= 0
# while i < total:
#     j = i
#     while j < total:
#         if lista[i] > lista[j]: 
#             aux = lista[i]		
#             lista[i] = lista[j]   
#             lista[j] = aux      
#         j= j+1
#     i=i+1
# print(lista)

# metodo de burbuja
# for n in lista:
#  	for n in range(0,len(lista)-1):
#  		if lista[n]>lista[n+1]:
#  			aux=lista.pop(n)
#  			lista.insert(n+2,aux)
# print(lista)


#metodo de inserccion
# a = 1
# b = 10
# a,b = b,a
# while i < total:
#     j = i
#     while j < total:
#         if lista[i] > lista[j]:
#             aux = lista[i]		
#             lista[i] = lista[j]   
#             lista[j] = aux 
#             print(lista)
     
#         j= j+1
#     i=i+1
# print(lista)





# 1. que el usuario engrese una frase y el programa diga cuantas a tiene
palabra = list(map(str,input("Ingrsa una palabra: ")))
i=0
a=0
while i<len(palabra) :
	if palabra[i] == "a" or palabra[i] == "A" :
		a=a+1
	i=i+1
print ("Tu numero de a es: ",a)

# 2 obtener la palabra mas larga

# 3 recibir varias palabras el programa devuelve las palabras como asteriscos
# 3 invertir la palabra ejem. BlisS=> SsilB
# lista = list(map(str,input("Ingrsa una palabra "))) 

# c=len(lista)-1
# for n in range(0,len(lista)-1):
# 	aux=lista.pop(0)
# 	lista.insert(c, aux)
# 	c=c-1
# print(lista)			



