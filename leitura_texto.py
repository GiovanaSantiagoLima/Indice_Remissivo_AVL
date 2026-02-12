def limpar_linha(linha):
    palavra = ""
    palavras = []
    for char in linha:
        if char.isalpha():
            palavra += char.lower()
        else:
            if palavra != "":
                palavras.append(palavra)
                palavra = ""
    if palavra != "":
        palavras.append(palavra)
    return palavras


def construir_indice(arvore, nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for numero_linha, linha in enumerate(arquivo, start=1):
            palavras = limpar_linha(linha)
            for palavra in palavras:
                arvore.total_palavras += 1
                arvore.inserir(palavra, numero_linha)
