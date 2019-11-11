# An extremely simple file reader module.

print("""Leitor de arquivos.

Digite o nome do arquivo:""")

arquivo = input("> ")
objetoarquivo = open(arquivo)

print("\nLeitura do arquivo:")

print(objetoarquivo.read())

objetoarquivo.close()
