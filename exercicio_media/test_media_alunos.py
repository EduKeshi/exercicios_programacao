from media_alunos import retorna_uma_lista_com_o_nome_dos_alunos_e_suas_medias, retorna_a_media_da_sala, retorna_a_menor_e_a_maior_media_da_sala, retorna_os_alunos_aprovados

def test_quando_o_nome_dos_alunos_forem_joao_da_silva_e_antonio_prado_e_as_medias_do_joao_forem_9_9_8_7_e_a_do_antonio_prado_10_10_9_6_deve_retornar_uma_lista_com_os_nomes_e_as_notas():
    lista_com_os_nomes_e_medias = retorna_uma_lista_com_o_nome_dos_alunos_e_suas_medias([8.25, 8.75], ["João da Silva", "Antonio Prado"])

    assert lista_com_os_nomes_e_medias == ['João da Silva ficou com a média 8.25', 'Antonio Prado ficou com a média 8.75']

def test_quando_as_medias_do_joao_forem_9_9_8_7_e_a_do_antonio_prado_10_10_9_6_deve_retornar_um_inteiro_com_as_medias_somadas_e_divididas():
    media_da_sala = retorna_a_media_da_sala([8.25, 8.75], 2)

    assert media_da_sala == 8.5

def test_quando_a_media_do_joao_for_8_25_e_a_do_antonio_for_8_75_deve_retornar_a_menor_media_8_25_e_a_maior_media_8_75():
    menor_media, maior_media = retorna_a_menor_e_a_maior_media_da_sala([8.25, 8.75])

    assert menor_media == 8.25
    assert maior_media == 8.75

def test_quando_a_media_for_maior_que_7_deve_retornar_joao_da_silva_e_antonio_prado_numa_lista():
    lista_alunos_aprovados = retorna_os_alunos_aprovados([8.25, 8.75], ["João da Silva", "Antonio Prado"])

    assert lista_alunos_aprovados == ['João da Silva', 'Antonio Prado']