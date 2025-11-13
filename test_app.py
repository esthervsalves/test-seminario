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