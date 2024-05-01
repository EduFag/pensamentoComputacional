import datetime
ANO_ATUAL = datetime.date.today().year

reprovados = 0
aprovados = 0
aprovados_ressalvas = 0

maior_renda = 0
maior_idade = 0

nome_maior_renda = None
nome_maior_idade = None

entrevistas = [
    # nome, ano_nasc, estuda, trabalha, renda
    # (listas)
]

for i in range(len(entrevistas)):
    nome = entrevistas[i][0]
    ano_nasc = int(entrevistas[i][1])
    idade = ANO_ATUAL - ano_nasc
    estuda = entrevistas[i][2]
    trabalha = entrevistas[i][3]
    renda = float(entrevistas[i][4])

    if (
        (trabalha == 'mei' and renda > 6750) or
        (trabalha == 'estag' and estuda == 'n') or 
        (idade < 14 and (trabalha == 'mei' or trabalha == 'estag' or trabalha == 'outro')) or 
        (idade < 0 or idade > 150) or 
        (renda < 0)
    ):
        reprovados = reprovados + 1
    elif (
        (trabalha == 'aposentado' and idade < 62) or 
        (idade < 14 and estuda == 'n') or 
        (trabalha == 's' and estuda == 's' and (idade >= 14 and idade <= 16))
    ):
        aprovados_ressalvas = aprovados_ressalvas + 1
    else:
        aprovados = aprovados + 1
        if trabalha == 'estag' and renda > maior_renda:
            maior_renda = renda
            nome_maior_renda = nome
        if (trabalha == 'estag' or trabalha == 'mei' or trabalha == 'outro') and idade > maior_idade:
            maior_idade = idade
            nome_maior_idade = nome

print('aprovados:', aprovados)
print('aprovados com ressalvas:', aprovados_ressalvas) 
print('reprovados:', reprovados)

if nome_maior_renda == None:
    print('nenhum usuário listado trabalha como estagiário')
else:
    print('estagiário com maior renda:',nome_maior_renda, ', renda: ', maior_renda)

print('pessoa mais velha que está trabalhando:', nome_maior_idade, ', idade: ', maior_idade)