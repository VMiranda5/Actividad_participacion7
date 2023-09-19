from modelo.elemento import Elemento, Conjunto

elemento1 = Elemento('elemtno1')
elemento2 = Elemento('elemtno2')
elemento3 = Elemento('elemtno3')
elemento4 = Elemento('elemtno4')
elemento5 = Elemento('elemtno5')
elemento6 = Elemento('elemtno6')
elemento7 = Elemento('elemtno7')
#print(elemento1==elemento2)

set1 = Conjunto('conj1')
set1.lista_elementos.append(elemento1)
set1.lista_elementos.append(elemento2)
set1.lista_elementos.append(elemento3)
set1.lista_elementos.append(elemento4)
set2 = Conjunto('conj2')
set2.lista_elementos.append(elemento3)
set2.lista_elementos.append(elemento3)
set2.lista_elementos.append(elemento7)
#print(set1.contiene(elemento3))
#set1.agregar_elemento(elemento4)
#print(set1.lista_elementos)
#print(set2.id)

#sum = set1+set2
#print(sum.lista_elementos)

result = Conjunto.intersectar(set1, set2)
#print(result.lista_elementos)
print(set2)