from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def mostrarAjuda():
    print("\nFormate a entrada em uma linha, separando cada parametro com o caractere \"|\"\n")
    print("Primeiro parametro: Informe o texto a ser cifrado em hexadecimal")
    print("Segundo parametro:  Informe a chave (16, 24 ou 32 bytes em hexadecimal)")
    print("Terceiro parametro: Informe a letra \"C\" para cifrar o texto claro ou a letra \"D\" para decifrar\n")


entrada = input()

if (entrada.lower() == "ajuda"):
    mostrarAjuda()

else:
    entrada = entrada.split("|")
    print()

    # Testa caso entrada tenha 3 partes
    if (len(entrada) == 3):
        texto, chave, modo = entrada
        modo = modo.upper()

        if len(chave) % 8 != 0:
            print("Sua chave é inválida")
        else:
            if modo == "C":
                chave = bytes.fromhex(chave)
                # Cria a cifra AES, utilizando a chave informada e com o modo ECB, que é o mais simples
                cifra = AES.new(chave, AES.MODE_ECB)

                texto = bytes.fromhex(texto)
                # Realiza a encriptação dos dados e adiciona padding caso necessário
                resultado = cifra.encrypt(pad(texto, AES.block_size))

                # Mostrando o resultado da cifra em hexadecimal
                print(hex(int.from_bytes(resultado, byteorder='big'))[2:])

            elif modo == "D":
                chave = bytes.fromhex(chave)
                # Cria a cifra AES, utilizando a chave informada e com o modo ECB, que é o mais simples
                cifra = AES.new(chave, AES.MODE_ECB)

                texto = bytes.fromhex(texto)
                # Realiza a encriptação dos dados e remove padding caso necessário
                resultado = unpad(cifra.decrypt(texto), AES.block_size)

                # Mostrando o resultado da decifragem em hexadecimal
                print(hex(int.from_bytes(resultado, byteorder='big'))[2:])
            else:
                print("O modo informado não existe")
    else:
        print("A sua entrada está incorreta, digite \"ajuda\" caso queira saber mais")

input()