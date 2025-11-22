import unittest
from Examen2 import MiClase

class TestMiClaseEncuentra(unittest.TestCase):

    def setUp(self):
        self.obj = MiClase(5, 120, 12, [], [])

    def test_encuentra_lista_invalida(self):
        lista = [1, 2, "tres", 4]
        with self.assertRaises(ValueError):
            self.obj.Encuentra(lista, 2)


if __name__ == "__main__":
    unittest.main()
