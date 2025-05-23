# Instalação de bibliotecas
!pip install -q pytest requests

import os

# Criação da pasta e arquivos de teste
os.makedirs("testes", exist_ok=True)

# Teste com requests e unittest
with open("testes/test_api_request.py", "w") as f:
    f.write("""
import requests
import unittest

class TestAPIRequest(unittest.TestCase):
    def test_status_code(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        self.assertEqual(response.status_code, 200)

    def test_response_is_list(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        self.assertIsInstance(response.json(), list)

    def test_first_item_has_id(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        first_item = response.json()[0]
        self.assertIn("id", first_item)

if __name__ == "__main__":
    unittest.main()
""")

# Teste com funções matemáticas
with open("testes/test_math_operations.py", "w") as f:
    f.write("""
import unittest

def somar(a, b):
    return a + b

def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

class TestMathOperations(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(somar(2, 3), 5)

    def test_divisao_valida(self):
        self.assertAlmostEqual(dividir(10, 2), 5)

    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)

if __name__ == "__main__":
    unittest.main()
""")

# Teste com listas e pytest
with open("testes/test_list_utils.py", "w") as f:
    f.write("""
def filtrar_pares(lista):
    return [x for x in lista if x % 2 == 0]

def test_filtrar_pares():
    assert filtrar_pares([1, 2, 3, 4]) == [2, 4]

def test_filtrar_pares_vazia():
    assert filtrar_pares([]) == []

def test_filtrar_pares_todos_impares():
    assert filtrar_pares([1, 3, 5]) == []

def test_filtrar_pares_negativos():
    assert filtrar_pares([-2, -3, -4]) == [-2, -4]
""")

# Execução dos testes com unittest
print("==== Executando unittest: test_math_operations ====")
!python3 testes/test_math_operations.py

print("\n==== Executando unittest: test_api_request ====")
!python3 testes/test_api_request.py

# Execução dos testes com pytest
print("\n==== Executando pytest: test_list_utils ====")
!pytest testes/test_list_utils.py
