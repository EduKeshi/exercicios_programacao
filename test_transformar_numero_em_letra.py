from transformar_numero_em_letra import descriptografando_numeros

def test_quando_os_numeros_forem_2_0_2_13_deve_retornar_dado():
    palavra = descriptografando_numeros("3 0 3 14")

    assert palavra == "DADO"

def test_quando_os_numeros_forem_2_0_2_7_14_17_17_14_deve_retornar_cachorro():
    palavra = descriptografando_numeros("2 0 2 7 14 17 17 14")

    assert palavra == "CACHORRO"

def test_quando_os_numeros_forem_0_21_8_0_14_deve_retornar_aviao():
    palavra = descriptografando_numeros("0 21 8 0 14")

    assert palavra == "AVIAO"

