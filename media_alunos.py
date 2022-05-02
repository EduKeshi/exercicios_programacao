def faz_as_fatias_da_minha_lista_de_medias(numero_de_alunos_da_sala: str, nome_alunos: list, media_dos_alunos: list):
    numero_de_medias_por_aluno = int(len(media_dos_alunos) / numero_de_alunos_da_sala)
    
    # Fazendo uma lista que vai receber as médias do aluno
    lista_notas_de_cada_aluno = []

    for fatias_cortadas, cada_aluno in enumerate(nome_alunos):
        inicio_da_fatia = fatias_cortadas * numero_de_medias_por_aluno
        final_da_fatia = numero_de_medias_por_aluno * (fatias_cortadas + 1)
        lista_notas_de_cada_aluno.append(media_dos_alunos[inicio_da_fatia:final_da_fatia])
    
    return lista_notas_de_cada_aluno, nome_alunos, numero_de_medias_por_aluno, numero_de_alunos_da_sala

def faz_a_lista_de_medias(lista_notas_de_cada_aluno: list, numero_de_medias_por_aluno: int):
    lista_de_medias = []
    # Pegando a média dos alunos
    for notas in lista_notas_de_cada_aluno:
        soma_das_medias = sum(notas)
        media_final = soma_das_medias / numero_de_medias_por_aluno
        lista_de_medias.append(media_final)

    return lista_de_medias
    
def retorna_uma_lista_com_o_nome_dos_alunos_e_suas_medias(lista_de_medias: list, nome_alunos: list):
    lista_com_os_nomes_e_medias = []
    for indice, media in enumerate(lista_de_medias):
        lista_com_os_nomes_e_medias.append(f"{nome_alunos[indice]} ficou com a média {media}")
    
    return lista_com_os_nomes_e_medias

def retorna_a_media_da_sala(lista_de_medias: list, numero_de_alunos_da_sala: int):
    soma_da_medias_dos_alunos = sum(lista_de_medias)
    media_da_sala = soma_da_medias_dos_alunos / numero_de_alunos_da_sala

    return media_da_sala

def retorna_a_menor_e_a_maior_media_da_sala(lista_de_medias: list):
    menor_media = min(lista_de_medias)
    maior_media = max(lista_de_medias)

    return menor_media, maior_media

def retorna_os_alunos_aprovados(lista_de_medias: list, nome_alunos: list):
    # Alunos que foram aprovados - funcionalidade 4
    lista_alunos_aprovados = []
    for indice, media in enumerate(lista_de_medias):
        if media >= 7:
            lista_alunos_aprovados.append(nome_alunos[indice])

    return lista_alunos_aprovados
        
if __name__ == "__main__":
    lista_notas_de_cada_aluno, nome_alunos, numero_de_medias_por_aluno, numero_de_alunos_da_sala = faz_as_fatias_da_minha_lista_de_medias(2, ["João da Silva", "Antonio Prado"], [9, 9, 8, 7, 10, 10, 9, 6])

    lista_de_medias = faz_a_lista_de_medias(lista_notas_de_cada_aluno, numero_de_medias_por_aluno)

    lista_com_os_nomes_e_medias = retorna_uma_lista_com_o_nome_dos_alunos_e_suas_medias(lista_de_medias, nome_alunos)
    
    media_da_sala = retorna_a_media_da_sala(lista_de_medias, numero_de_alunos_da_sala)

    menor_media, maior_media = retorna_a_menor_e_a_maior_media_da_sala(lista_de_medias)

    lista_alunos_aprovados = retorna_os_alunos_aprovados(lista_de_medias, nome_alunos)
    
    print(f"\nMédias: {lista_com_os_nomes_e_medias}")
    print(f"\nMédia da sala {media_da_sala}")
    print(f"\nA menor média da sala foi {menor_media}")
    print(f"\nA Menor média da sala foi {maior_media}")
    print(f"\nAlunos aprovados {lista_alunos_aprovados}")