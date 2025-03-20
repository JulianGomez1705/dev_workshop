class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        """
        Invierte el orden de los elementos en una lista sin usar reversed() o lista[::-1].
        """
        if not isinstance(lista, list):
            raise TypeError("El argumento debe ser una lista")
        
        lista_invertida = []
        for i in range(len(lista) - 1, -1, -1):
            lista_invertida.append(lista[i])
        
        return lista_invertida
    
    def buscar_elemento(self, lista, elemento):
        """
        Busca un elemento en una lista y devuelve su índice (o -1 si no existe).
        """
        if not isinstance(lista, list):
            raise TypeError("El argumento debe ser una lista")
        
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1
    
    def eliminar_duplicados(self, lista):
        """
        Elimina elementos duplicados de una lista sin usar set().
        """
        result = []
        for item in lista:
            if not any(item is x for x in result):
                result.append(item)
            return result
        pass
    
    def merge_ordenado(self, lista1, lista2):
        """
        Combina dos listas ordenadas en una sola lista ordenada.
        """
        if not isinstance(lista1, list) or not isinstance(lista2, list):
            raise TypeError("Ambos argumentos deben ser listas")
        
        resultado = []
        i, j = 0, 0
        
        while i < len(lista1) and j < len(lista2):
            if lista1[i] < lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1
        
        resultado.extend(lista1[i:])
        resultado.extend(lista2[j:])
        
        return resultado
    
    def rotar_lista(self, lista, k):
        """
        Rota los elementos de una lista k posiciones a la derecha.
        """
        if not isinstance(lista, list) or not isinstance(k, int):
            raise TypeError("Los argumentos deben ser una lista y un entero")
        
        if not lista:
            return lista
        
        k = k % len(lista)
        return lista[-k:] + lista[:-k]
    
    def encuentra_numero_faltante(self, lista):
        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        """
        if not isinstance(lista, list):
            raise TypeError("El argumento debe ser una lista")
        
        n = len(lista) + 1
        suma_esperada = n * (n + 1) // 2
        suma_real = sum(lista)
        
        return suma_esperada - suma_real
    
    def es_subconjunto(self, conjunto1, conjunto2):
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        """
        if not isinstance(conjunto1, list) or not isinstance(conjunto2, list):
            raise TypeError("Ambos argumentos deben ser listas")
        
        for elemento in conjunto1:
            if elemento not in conjunto2:
                return False
        return True
    
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        """
        pila = []
        
        def push(elemento):
            pila.append(elemento)
        
        def pop():
            if not pila:
                return None
            return pila.pop()
        
        def peek():
            if not pila:
                return None
            return pila[-1]
        
        def is_empty():
            return len(pila) == 0
        
        return {"push": push, "pop": pop, "peek": peek, "is_empty": is_empty}
    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        """
        cola = []
        
        def enqueue(elemento):
            cola.append(elemento)
        
        def dequeue():
            if not cola:
                return None
            return cola.pop(0)
        
        def peek():
            if not cola:
                return None
            return cola[0]
        
        def is_empty():
            return len(cola) == 0
        
        return {"enqueue": enqueue, "dequeue": dequeue, "peek": peek, "is_empty": is_empty}
    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        """
        
        if not matriz:
            return []  # Caso de matriz vacía
        return [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]