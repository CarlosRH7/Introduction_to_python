# lista = list(map(int,input("Dame una lista nuemrica separado de una coma: ").split(",")))
# print ("Esta es tu lista:",lista)
# total = len(lista)
# i=0
# j=1
# while j < total:
# 	if lista[i] > lista[j]: 
# 	    aux = lista[i]		
# 	    lista[i] = lista[j]   
# 	    lista[j] = aux 
# 	    print (lista)
#     j=j+2
# 	i=i+2
	     
 	   
# print ("Tu lista ordenada de menor a mayor es: ",lista)


#metodo de inserccion
# lista = [2,5,1,4,5,9,7,8,6]

# for i in range(1,len(lista)):
# 	j=i
# 	while j>0 and lista[j]<lista[j-1]:
# 		lista[j],lista[j-1]=lista[j-1],lista[j]
# 		j-=1
# 		print(lista)


#metodo de inserccion invertida
lista = [2,5,1,4,5,9,7,8,6]

for i in range(1,len(lista)):
	j=i
	while j>0 and lista[j]<lista[j-1]:
		lista[j],lista[j-1]=lista[j-1],lista[j]
		j-=1
		print(lista)
