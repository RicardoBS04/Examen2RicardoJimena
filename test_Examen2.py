import unittest
from Examen2 import MiClase

class TestMiClase(unittest.TestCase):

    def setUp(self):
        self.obj = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])

    # PRUEBA 1 assertGreater 
    def test_valencia_mayor_que_cero(self):
        resultado = self.obj.ObtieneValencia(13579) 
        self.assertGreater(resultado, 11) #Cambio para que falle la prueba 

    # PRUEBA 2 assertIsNone
    def test_mas_bailable_lista_vacia(self):
        resultado = self.obj.ObtieneMasBailable([])
        self.assertIsNone(resultado) 
 

if __name__ == "__main__":
    unittest.main()
