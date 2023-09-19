from dataclasses import dataclass


@dataclass
class Elemento:
    nombre:str

    def __eq__(self, other):
        return self.nombre == other.nombre
    
class Conjunto:
    
    contador = 0

    def __init__(self, nombre:str):
        self.lista_elementos: list['Elemento']=[]
        self.nombre: str = nombre
        self.__class__.contador +=1
        self.__id = self.__class__.contador

    @property
    def id(self):
        return self.__id
    
    def contiene(self, elemento:'Elemento')->bool:
        return elemento in self.lista_elementos

    def agregar_elemento(self, elemento:'Elemento'):
        if not self.contiene(elemento):
            self.lista_elementos.append(elemento)
    
    def __add__(self,other:'Conjunto'):
        for i in other.lista_elementos:
            if not i in self.lista_elementos:
                self.lista_elementos.append(i)
        return self
    
    @classmethod
    def intersectar(cls,conjunto1: 'Conjunto', conjunto2: 'Conjunto'):
        resultado: 'Conjunto'= Conjunto(conjunto1.nombre+' INTERSECTADO '+conjunto2.nombre)
        for i in conjunto1.lista_elementos:
            if conjunto2.contiene(i):
                resultado.lista_elementos.append(i)
        return resultado

    def __str__(self) -> str:
        nombres_elementos =''
        for i in self.lista_elementos:
            nombres_elementos+=(i.nombre+',')
        return f'Conjunto {self.nombre}: ({nombres_elementos})'