class TremAutonomo:
    def __init__(self):
        self.posicao = 0
        self.movimentos_consecutivos = 0
        self.direcao_anterior = None

    def mover(self, comandos):
        if not comandos:
            raise ValueError("A lista de comandos não pode ser vazia.")
        
        if len(comandos) > 50:
            raise ValueError("A lista de comandos não pode exceder 50 movimentos.")

        posicao_inicial = self.posicao

        for comando in comandos:
            if comando not in ["ESQUERDA", "DIREITA"]:
                raise ValueError(f"Comando inválido: {comando}")

            if self.direcao_anterior == comando:
                self.movimentos_consecutivos += 1
            else:
                self.movimentos_consecutivos = 1
                self.direcao_anterior = comando

            if self.movimentos_consecutivos > 20:
                raise ValueError("O trem não pode fazer mais de 20 movimentos consecutivos na mesma direção.")

            if comando == "ESQUERDA":
                self.posicao -= 1
            elif comando == "DIREITA":
                self.posicao += 1

            if abs(self.posicao - posicao_inicial) > 50:
                raise ValueError("O trem não pode percorrer mais de 50 posições por viagem.")

        return self.posicao

import unittest

class TestTremAutonomo(unittest.TestCase):
    def setUp(self):
        self.trem = TremAutonomo()

    def test_movimentos_basicos(self):
        self.assertEqual(self.trem.mover(["DIREITA", "DIREITA"]), 2)
        self.trem.posicao = 0
        self.assertEqual(self.trem.mover(["ESQUERDA"]), -1)
        self.trem.posicao = 0
        self.assertEqual(self.trem.mover(["ESQUERDA", "DIREITA", "DIREITA", "DIREITA", "DIREITA", "ESQUERDA"]), 2)

    def test_comandos_invalidos(self):
        with self.assertRaises(ValueError):
            self.trem.mover(["UP", "DIREITA"])
        with self.assertRaises(ValueError):
            self.trem.mover(["esquerda"])

    def test_excesso_de_movimentos(self):
        with self.assertRaises(ValueError):
            self.trem.mover(["DIREITA"] * 21)
        with self.assertRaises(ValueError):
            self.trem.mover(["DIREITA"] * 51)

if __name__ == "__main__":
    unittest.main()
