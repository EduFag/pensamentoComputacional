POS_LETRA_A = 65
POS_LETRA_Z = 90
NUM_LETRAS_ALFABETO = 26

texto_original = input('digite um texto em caixa alta para ser cifrado: ')

SHIFT = 3
texto_cifrado = ''

for char in texto_original:
    if POS_LETRA_A <= ord(char) <= POS_LETRA_Z:
        shifted_char = chr(
            (ord(char) - POS_LETRA_A + SHIFT) % NUM_LETRAS_ALFABETO + POS_LETRA_A
        )
        texto_cifrado += shifted_char
    else:
        texto_cifrado += char

print('texto cifrado:', texto_cifrado)
print('texto decifrado:', texto_original)