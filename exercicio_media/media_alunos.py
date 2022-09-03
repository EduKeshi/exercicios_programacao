def faz_a_media_individual(notas_do_aluno: str):
    lista_com_as_notas_dos_alunos = notas_do_aluno.split(" ")
    soma_das_notas = 0

    for nota in lista_com_as_notas_dos_alunos:
        soma_das_notas += int(nota)

    media_dos_alunos = soma_das_notas / 4

    return media_dos_alunos


def faz_a_media_da_sala(notas_dos_alunos: list, numero_de_alunos_da_sala: int):
    soma_das_notas = 0
    numero_de_notas = 4 * numero_de_alunos_da_sala

    for lista_com_notas in notas_dos_alunos:
        lista_com_as_notas_dos_alunos = lista_com_notas.split(" ")
        for nota_individual in lista_com_as_notas_dos_alunos:
            soma_das_notas += int(nota_individual)

    media_da_sala = soma_das_notas / numero_de_notas

    return media_da_sala


def faz_o_sort_pelo_segundo_valor_da_tupla(tupla: tuple):
    return tupla[1]


def faz_as_perguntas_pro_usuario_e_monta_o_dicionario_com_as_informacoes():
    quantidade_de_alunos_da_sala = int(input("Quantos alunos tem na sala?\n -"))

    dobro_da_quantidade_de_alunos = quantidade_de_alunos_da_sala * quantidade_de_alunos_da_sala
    dicionario_com_as_informacoes = {"numero de alunos": quantidade_de_alunos_da_sala,
                                     "nome dos alunos": [],
                                     "nota dos alunos": []
                                     }

    for indice in range(dobro_da_quantidade_de_alunos):
        if indice >= quantidade_de_alunos_da_sala:
            nota_do_aluno = input("Qual a nota do aluno? (ordem de nomes colocados)\n -")
            dicionario_com_as_informacoes["nota dos alunos"].append(nota_do_aluno)
            continue

        nome_dos_alunos = input("Qual o nome do aluno?\n -")
        dicionario_com_as_informacoes["nome dos alunos"].append(nome_dos_alunos)

    return dicionario_com_as_informacoes


def retorna_uma_lista_de_tuplas_com_o_nome_dos_alunos_e_suas_medias(dicionario_com_as_informacoes: dict):
    lista_de_tuplas_com_os_nomes_e_medias = []

    for indice, nome in enumerate(dicionario_com_as_informacoes["nome dos alunos"]):
        media_do_aluno = faz_a_media_individual(dicionario_com_as_informacoes["nota dos alunos"][indice])
        lista_de_tuplas_com_os_nomes_e_medias.append((nome, media_do_aluno))

    return lista_de_tuplas_com_os_nomes_e_medias


def retorna_a_media_da_sala(dicionario_com_as_informacoes: dict):
    nota_dos_alunos = dicionario_com_as_informacoes["nota dos alunos"]
    numero_de_alunos_da_sala = dicionario_com_as_informacoes["numero de alunos"]

    media_da_sala = faz_a_media_da_sala(nota_dos_alunos, numero_de_alunos_da_sala)

    return media_da_sala


def retorna_a_menor_e_a_maior_media_da_sala(dicionario_com_as_informacoes: dict):
    lista_de_tuplas_com_os_nomes_e_medias = retorna_uma_lista_de_tuplas_com_o_nome_dos_alunos_e_suas_medias(dicionario_com_as_informacoes)
    lista_de_tuplas_com_os_nomes_e_medias.sort(key=faz_o_sort_pelo_segundo_valor_da_tupla)

    menor_media = lista_de_tuplas_com_os_nomes_e_medias[0][1]
    maior_media = lista_de_tuplas_com_os_nomes_e_medias[-1][1]

    return menor_media, maior_media


def retorna_os_alunos_aprovados(dicionario_com_as_informacoes: dict):
    lista_de_tuplas_com_os_alunos_aprovados = retorna_uma_lista_de_tuplas_com_o_nome_dos_alunos_e_suas_medias(dicionario_com_as_informacoes)

    for indice, tupla_com_nome_e_media in enumerate(lista_de_tuplas_com_os_alunos_aprovados):
        if tupla_com_nome_e_media[1] >= 7:
            continue

        lista_de_tuplas_com_os_alunos_aprovados.pop(indice)

    return lista_de_tuplas_com_os_alunos_aprovados


if __name__ == "__main__":
    dicionario_com_todas_as_informacoes = faz_as_perguntas_pro_usuario_e_monta_o_dicionario_com_as_informacoes()
    lista_de_tuplas_com_nome_e_media_dos_alunos = retorna_uma_lista_de_tuplas_com_o_nome_dos_alunos_e_suas_medias(dicionario_com_todas_as_informacoes)
    menor_media_da_sala,  maior_media_da_sala= retorna_a_menor_e_a_maior_media_da_sala(dicionario_com_todas_as_informacoes)
    lista_de_tuplas_com_alunos_aprovados = retorna_os_alunos_aprovados(dicionario_com_todas_as_informacoes)

    print(lista_de_tuplas_com_alunos_aprovados)
    print(menor_media_da_sala, "-", maior_media_da_sala)
    print(lista_de_tuplas_com_alunos_aprovados)


