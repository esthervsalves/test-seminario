from app import soma, subtrai, multiplica, divide

def test_soma_correta():
    # Testa se a função soma está correta
    assert soma(1, 2) == 3
    assert soma(-1, 1) == 0

def test_subtrai_correta():
    # Testa se a função subtrai está correta
    assert subtrai(5, 2) == 3
    assert subtrai(10, 5) == 5
    assert subtrai(2, 5) == -3

def test_multiplica_correta():
    # Testa se a função multiplica está correta
    assert multiplica(3, 4) == 12
    assert multiplica(-2, 3) == -6
    assert multiplica(0, 5) == 0

def test_soma_incorreta():
    # Testa um caso incorreto para a função soma
    assert soma(2, 2) != 5

def test_subtrai_incorreta():
    # Testa um caso incorreto para a função subtrai
    assert subtrai(5, 3) != 1

def divide(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b