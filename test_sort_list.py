import unittest

# Aca traemos la función que vamos a probar
def sort_list(input_list):
    for i in range(len(input_list)):
        for j in range(len(input_list) - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
    return input_list

# Ejecutamos los casos de prueba creando una clase

class TestSortList(unittest.TestCase):

    def test_lista_negativos(self):
        self.assertEqual(sort_list([-1, -3, 0, 1]), [-3, -1, 0, 1])

    def test_lista_desordenada(self):
        self.assertEqual(sort_list([25, 20, 15, 10]), [10, 15, 20, 25])

    def test_lista_con_duplicados(self):
        self.assertEqual(sort_list([3, 1, 2, 3]), [1, 2, 3, 3])

    def test_lista_vacia(self):
        self.assertEqual(sort_list([]), [])

    def test_lista_decimales(self):
        self.assertEqual(sort_list([1.2, 3.6, 2.5, 2.3]), [1.2, 2.3, 2.5, 3.6])        


# Este bloque permite ejecutar el test directamente
if __name__ == '__main__':
    unittest.main()

# Y en efecto, todos los casos de prueba que se probaron dieron como resultado OK