# Exercício 1 -> Descriptografando
Uma das maneiras mais eficientes para se fazer comunicação entre partes, de modo que somente o escritor e leitor possam entender a mensagem é encriptar (criptografar) as mensagens.
Para tal, há diversas maneiras de se fazer isso. Cada uma delas possui seus tradeoffs. Algumas são relativamente fáceis de se implementar, porém relativamente simples de quebrar a criptografia (quebra de criptogafia: um terceiro pode ler a mensagem).

Assim, você Edudardo Keschichian, como Engenheiro de Software, ficou encarregado de implementar um subprograma (console application) resposável por fazer a leitura de uma palavra criptografada e descriptografá-la.
Entrada: Um número de 0 a 25, onde 0 representa a letra "A" e 25 representa a letra "Z" (sempre em letra maiúscula).
Saída: A palavra descriptografada.

Exemplo:

ENTRADA: 3 0 3 14 

SAÍDA: DADO
<br>
# Exercício 2 -> Calcula Média 
John Gordinho é professor de física em uma escola estadual. Ele é apaixonado por seus alunos e sempre busca desenvolvê-los. Para tal, ele utiliza como metodologia de avaliação bimestral, o cálculo da média de todas as avaliações (prova, trabalho individual, trabalho em dupla) aplicadas nos alunos. Assim sendo, John Gordinho contratou você, Edu, para escrever um programa (console application) para auxiliá-lo nesse processo. Ele pediu os seguintes requisitos: 
- A primeira entra do subprograma é um número inteiro de 0 a 50, representando o número "A" de alunos na sala 
- Para cada "A" valores, o usuário poderá escrever o nome dos alunos 
- Para cada aluno gravado, deverá ser informado as notas que ess esse aluno recebeu na avaliação. A ordem dos alunos deverá seguir a ordem de cadastro do nome dos alunos.

Exemplo: 
- 2 
- João da Silva 
- Antônio Prado
- 9 9 8 7 (média do João)
- 10 10 9 6 (média do Antônio Prado)

SAÍDA:<br>
**Funcionalidade 1**: O subprograma deverá imprimir o nome dos alunos, bem como a sua respectiva média.<br> 
**Funcionalidade 2**: O subprograma deverá imprimir a média da sala. <br>
**Funcionalidade 3**: O subprograma deverá imprimir a média mínima (menor média perante a média da sala) e a média máxima (maior média perante a média da sala).<br>
**Funcionalidade 4**: O subprograma deverá imprimir os alunos que foram aprovados (média maior ou igual a 7).<br>
