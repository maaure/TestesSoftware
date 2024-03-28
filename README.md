# Testes de Unidade para a Classe Triangulo

Este documento descreve os testes de unidade para a classe `Triangulo`

## Valida Forma

| Variáveis de Entrada       | Classes Válidas                             | Classes Inválidas                           |
| -------------------------- | ------------------------------------------- | ------------------------------------------- |
| Tamanho dos lados a, b e c | a + b < c **ou** b + c < a **ou** c + a < b | a + b > c **ou** b + c > a **ou** c + a > b |
|                            | a > 0 <br> b > 0 <br> c > 0                 | a ≤ 0 <br> b ≤ 0 <br> c ≤ 0                 |

### Testes

```python
def test_validar_forma(self):
    t1 = Triangulo(3, 4, 5)
    self.assertTrue(t1.validar_forma())

    t2 = Triangulo(1, 1, 3)
    self.assertFalse(t2.validar_forma())

    t2 = Triangulo(3, 1, 1)
    self.assertFalse(t2.validar_forma())

    t3 = Triangulo(1, 3, 1)
    self.assertFalse(t3.validar_forma())

    t4 = Triangulo(-1, 1, 1)
    self.assertFalse(t4.validar_forma())

    t5 = Triangulo(1, -1, 1)
    self.assertFalse(t5.validar_forma())

    t6 = Triangulo(1, 1, -1)
    self.assertFalse(t6.validar_forma())
```

## É isósceles

| Variáveis de Entrada       | Classes Válidas                                                 | Classes Inválidas             |
| -------------------------- | --------------------------------------------------------------- | ----------------------------- |
| Tamanho dos lados a, b e c | a = b **e** b ≠ c <br> b = c **e** c ≠ a <br> c = a **e** a ≠ b | a ≠ b **e** b ≠ c **e** c ≠ a |

### Testes

```python
def test_eh_isosceles(self):
    t1 = Triangulo(3, 3, 2)
    self.assertTrue(t1.eh_isosceles())

    t2 = Triangulo(2, 3, 3)
    self.assertTrue(t2.eh_isosceles())

    t3 = Triangulo(2, 3, 2)
    self.assertTrue(t3.eh_isosceles())

    t4 = Triangulo(3, 3, 3)
    self.assertTrue(t4.eh_isosceles())

    t5 = Triangulo(3, 4, 5)
    self.assertFalse(t5.eh_isosceles())
```

## É equilátero

| Variáveis de Entrada       | Classes Válidas   | Classes Inválidas           |
| -------------------------- | ----------------- | --------------------------- |
| Tamanho dos lados a, b e c | a = b **e** b = c | a ≠ b <br> b ≠ c <br> c ≠ a |

### Testes

```python
def test_eh_equilatero(self):
    t1 = Triangulo(3, 3, 3)
    self.assertTrue(t1.eh_equilatero())

    t2 = Triangulo(3, 3, 5)
    self.assertFalse(t2.eh_equilatero())

    t3 = Triangulo(3, 4, 3)
    self.assertFalse(t3.eh_equilatero())

    t4 = Triangulo(3, 4, 4)
    self.assertFalse(t4.eh_equilatero())
```

## É escaleno

| Variáveis de Entrada       | Classes Válidas   | Classes Inválidas           |
| -------------------------- | ----------------- | --------------------------- |
| Tamanho dos lados a, b e c | a ≠ b **e** b ≠ c | a = b <br> b = c <br> c = a |

### Testes

```python
def test_eh_escaleno(self):
    t1 = Triangulo(3, 4, 5)
    self.assertTrue(t1.eh_escaleno())

    t2 = Triangulo(3, 3, 3)
    self.assertFalse(t2.eh_escaleno())

    t3 = Triangulo(3, 4, 3)
    self.assertFalse(t3.eh_escaleno())

    t4 = Triangulo(3, 4, 4)
    self.assertFalse(t4.eh_escaleno())

    t5 = Triangulo(3, 3, 5)
    self.assertFalse(t5.eh_escaleno())
```
