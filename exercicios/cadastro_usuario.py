# nome
nome = input('digite o seu nome:')
nome_cap = nome.capitalize()
nome_replace = nome.replace("", "-")
lista_nome = nome_replace.split("-")

while (
    (len(lista_nome) - 2 < 3) or 
    (nome != nome_cap) or 
    ('1' in lista_nome) or
    ('2' in lista_nome) or
    ('3' in lista_nome) or
    ('4' in lista_nome) or
    ('5' in lista_nome) or
    ('6' in lista_nome) or
    ('7' in lista_nome) or
    ('8' in lista_nome) or
    ('9' in lista_nome) == True
    ):
    nome = input('digite um nome válido:')
    nome_cap = nome.capitalize()
    nome_replace = nome.replace("", "-")
    lista_nome = nome_replace.split("-")

# sobrenome
sobrenome = input('digite o seu sobrenome:')
sobrenome_cap = sobrenome.capitalize()
sobrenome_replace = sobrenome.replace("", "-")
lista_sobrenome = sobrenome_replace.split("-")

while (
    (len(lista_sobrenome) - 2 < 3) or 
    (sobrenome != sobrenome_cap) or 
    ('1' in lista_sobrenome) or
    ('2' in lista_sobrenome) or
    ('3' in lista_sobrenome) or
    ('4' in lista_sobrenome) or
    ('5' in lista_sobrenome) or
    ('6' in lista_sobrenome) or
    ('7' in lista_sobrenome) or
    ('8' in lista_sobrenome) or
    ('9' in lista_sobrenome) == True
    ):
    sobrenome = input('digite um sobrenome válido:')
    sobrenome_cap = sobrenome.capitalize()
    sobrenome_replace = sobrenome.replace("", "-")
    lista_sobrenome = sobrenome_replace.split("-")

# email
email = input('digite seu email:')
email_replace = email.replace("", "-")
lista_email = email_replace.split("-")

while ('@' in lista_email) == False:
    email = input('digite um email válido:')
    email_replace = email.replace("", "-")
    lista_email = email_replace.split("-")

lista_email_nomesite = email.split("@")
email_nome = lista_email_nomesite[0]
email_site = lista_email_nomesite[1]

email_nome_replace = email_nome.replace("", "-")
lista_email_nome = email_nome_replace.split("-")

email_site_replace = email_site.replace("", "-")
lista_email_site = email_site_replace.split("-")

while (
    (len(lista_email_nome) - 2 < 3 or len(lista_email_nome) > 30) or
    (len(lista_email_site) + 2 < 4 or len(lista_email_site) > 20) or
    (email_site[(len(lista_email_site) - 6):] != '.com') 
):
    email = input('digite um email válido:')
    email_replace = email.replace("", "-")
    lista_email = email_replace.split("-")

    while ('@' in lista_email) == False:
        email = input('digite um email válido:')
        email_replace = email.replace("", "-")
        lista_email = email_replace.split("-")

    lista_email_nomesite = email.split("@")
    email_nome = lista_email_nomesite[0]
    email_site = lista_email_nomesite[1]

    email_nome_replace = email_nome.replace("", "-")
    lista_email_nome = email_nome_replace.split("-")

    email_site_replace = email_site.replace("", "-")
    lista_email_site = email_site_replace.split("-")

print('cadastro aprovado')