from arvore_avl import AVL
from leitura_texto import construir_indice

def main():
    arvore = AVL()

    construir_indice(arvore, "texto_origem.txt")
    print("Busca por palavra:")
    resultado = arvore.buscar("algoritmo")
    if resultado == -1:
        print("Palavra não encontrada.")
    elif resultado == 0:
        print("Palavra encontrada. ME = 0.")
    else:
        print("Palavra encontrada com ME diferente de zero.")
    print("\nBusca por prefixo 'alg':")
    print(arvore.busca_prefixo("alg"))
    print("\nPalavra mais frequente:")
    print(arvore.palavra_mais_frequente())
    arvore.imprimir_indice("indice_saida.txt")
    print("\nÍndice gerado com sucesso.")

if __name__ == "__main__":
    main()
