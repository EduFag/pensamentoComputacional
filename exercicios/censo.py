ano_nascimento = int(input('digite o ano do seu nascimento: '))
import datetime
ANO_ATUAL = datetime.date.today().year
idade = ANO_ATUAL - ano_nascimento
estudo = input('estuda(s/n)? ')
trabalho = input('trabalha(s/n)? ')
if trabalho == 's':
    regime = input('qual regime(mei/estag/outro)? ')
    renda = float(input('qual sua renda? '))
    aposentadoria = ''
else:
    regime = ''
    renda = 0
    aposentadoria = input('aposentado(s/n)? ')

if (regime == 'mei' and renda > 6750) or (regime == 'estag' and estudo == 'n') or (idade < 14 and trabalho == 's') or (idade < 0 or idade > 150) or (renda < 0):
    print('cadastro reprovado')
elif (aposentadoria == 's' and idade < 62) or (idade < 14 and estudo == 'n') or (trabalho == 's' and estudo == 's' and (idade >= 14 and idade <= 16)):
    print('cadastro aprovado com ressalvas')
else:
    print('cadastro aprovado')