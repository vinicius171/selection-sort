import random

def gerar_lista_aleatoria_e_salvar_arquivo(tamanho=10, nome_arquivo="lista_gerada.txt"):
    lista_aleatoria = []
    for _ in range(tamanho):
        numero = random.randint(-100, 100)
        lista_aleatoria.append(numero)
    
    with open(nome_arquivo, 'w') as arquivo:
        for numero in lista_aleatoria:
            arquivo.write(str(numero) + '\n')

    return lista_aleatoria

tamanho_da_lista = 1000
nome_arquivo = "lista_gerada4.txt"
lista_aleatoria = gerar_lista_aleatoria_e_salvar_arquivo(tamanho_da_lista, nome_arquivo)
print(f"Lista gerada e salva no arquivo '{nome_arquivo}':")
