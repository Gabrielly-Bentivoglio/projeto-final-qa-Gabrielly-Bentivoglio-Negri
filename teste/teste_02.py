# Cria a pasta se não existir
import os
os.makedirs("testes", exist_ok=True)

# Cria o arquivo com a função e os testes
with open("testes/test_eh_primo.py", "w") as f:
    f.write("""
import unittest

def eh_primo(n):
    \"\"\"Verifica se um número é primo.\"\"\"
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

class TestEhPrimo(unittest.TestCase):
    def test_numero_primo(self):
        self.assertTrue(eh_primo(7))

    def test_numero_nao_primo(self):
        self.assertFalse(eh_primo(8))

    def test_numero_1_nao_primo(self):
        self.assertFalse(eh_primo(1))

    def test_numero_2_primo(self):
        self.assertTrue(eh_primo(2))

if __name__ == "__main__":
    unittest.main()
""")

# Roda o teste
!python3 testes/test_eh_primo.py
