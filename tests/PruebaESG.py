import unittest
import math
from src.logica.ESG import ESG
class PruebaESG(unittest.TestCase):
    # Casos de prueba números reales
    def test_ESG_parametrosNumericos_raicesReales(self):
        # arrange
        a = 3
        b = -5
        c = 1
        x1Esperado = 1.43
        x2Esperado = 0.23

        # Do
        ecuacion = ESG()
        x1Actual, x2Actual = ecuacion.calculoECS(a, b, c)


        # Assert
        precision = math.fabs(x1Esperado - x1Actual)
        self.assertLessEqual(precision,0.01)
        precision = math.fabs(x2Esperado - x2Actual)
        self.assertLessEqual(precision, 0.01)

    def test_ESG_parametrosNumericosMultiple_raicesReales(self):
        # arragbe
        ecuacion = ESG()
        items = (
            {"Case": "Caso 01", "a": 3, "b": -5, "c": 1, "RaizEsperada1": 1.43, "RaizEsperada2": 0.23},
            {"Case": "Caso 02", "a": 1, "b": 2, "c": 1, "RaizEsperada1": -1.00, "RaizEsperada2": -1.00},
            {"Case": "Caso 03", "a": -1, "b": 2, "c": -1, "RaizEsperada1": 1.0, "RaizEsperada2": 1.00},
            {"Case": "Caso 04", "a": 1, "b": 0, "c": -18, "RaizEsperada1": 4.2, "RaizEsperada2": -4.24},
            {"Case": "Caso 05", "a": 1, "b": 4, "c": 0, "RaizEsperada1": 0.0, "RaizEsperada2": -4.00},
            {"Case": "Caso 06", "a": 1, "b": 4, "c": 4, "RaizEsperada1": -2.0, "RaizEsperada2": -2.00},
            {"Case": "Caso 07", "a": 1, "b": 3, "c": 2, "RaizEsperada1": -1.0, "RaizEsperada2": -2.00},
        )

        # do
        for item in items:
            with self.subTest(item["Case"]):
                RaizActual1, RaizActual2 = ecuacion.calculoECS(item["a"], item["b"], item["c"])

        # assert
        precision = math.fabs(item["RaizEsperada1"] - RaizActual1)
        self.assertLessEqual(precision, 0.01)
        precision = math.fabs(item["RaizEsperada2"] - RaizActual2)
        self.assertLessEqual(precision, 0.01)

#Casos de prueba de números imaginarios
    def test_solucionESG_parametrosNumericos_raicesComplejasConjugadas(self):
        # Arrange
        # Arrange
        ecuacionSegundoGrado = ESG()

        items = (
            {"Case": "Caso 01", "a": 1, "b": 1, "c": 1, "RaizEsperada1": "-0.50+0.87i", "RaizEsperada2": "-0.50-0.87i"},
            {"Case": "Caso 02", "a": 1, "b": 2, "c": 3, "RaizEsperada1": "-1.00+1.41i", "RaizEsperada2": "-1.00-1.41i"},
        )

        # Do
        for item in items:
            with self.subTest(item["Case"]):
                ecuacionSegundoGrado.definirParametros(item["a"], item["b"], item["c"])
            RaizActual1, RaizActual2 = ecuacionSegundoGrado.solucionESG()

            # Assert
            self.assertEqual(item["RaizEsperada1"], RaizActual1)
            self.assertEqual(item["RaizEsperada2"], RaizActual2)

#Casos de prueba de alfanuméricos
    def test_solucionESG_parametrosNoNumericos_lanzaException(self):
        # Arrange
        ecuacionSegundoGrado = ESG()
        items = (
            {"Case": "Caso 01", "a": "a", "b": "b", "c": "c"},
            {"Case": "Caso 02", "a": "a", "b": 1, "c": 1},
            {"Case": "Caso 03", "a": 1, "b": "aa", "c": 1},
            {"Case": "Caso 03", "a": 1, "b": "3,1", "c": 1},
        )

        for item in items:
            with self.subTest(item["Case"]):
                self.assertTrue(True)
                with self.assertRaises(ValueError):
                    ecuacionSegundoGrado.definirParametros(item["a"], item["b"], item["c"])

        # Assert
        self.assertTrue(True)
        with self.assertRaises(ValueError):
            ecuacionSegundoGrado.definirParametros("3.1", "2", "c")