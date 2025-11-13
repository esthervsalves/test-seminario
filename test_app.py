from app import soma, subtrai

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