import unittest
from Examen2 import MiClase    # cámbialo si tu archivo se llama diferente


class TestMiClase(unittest.TestCase):

    def setUp(self):
        self.obj = MiClase(
            5,
            120,
            12,
            ["Canción 1", "Canción 2", "Canción 3"],
            [0.8, 0.9, 0.7]
        )

    # ============================
    # PRUEBA 1 (assertGreater)
    # ============================
    def test_divisores_cantidad_mayor_que_uno(self):
        """DivisibleTempo debe devolver más de un divisor en números compuestos."""
        resultado = self.obj.DivisibleTempo(12)   # divisores: 1,2,3,4,6,12 → 6 divisores
        self.assertGreater(len(resultado), 1)

    # ============================
    # PRUEBA 2 (assertIsNone)
    # ============================
    def test_mas_bailable_lista_negativa(self):
        """ObtieneMasBailable debería retornar None si la lista es None (caso inválido)."""
        resultado = self.obj.ObtieneMasBailable(None)
        self.assertIsNone(resultado)


if __name__ == "__main__":
    unittest.main()
