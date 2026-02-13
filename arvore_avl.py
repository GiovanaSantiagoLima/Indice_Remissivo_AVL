from no_avl import NO
class AVL:

    def __init__(self):
        self.raiz = None
        self.total_palavras = 0
        self.total_descartadas = 0
        self.rotacoes = 0
        self.tempo_construcao = 0.0

# FUNÇÕES AUXILIARES DA AVL
    def altura(self, no):
        if not no:
            return 0
        return no.altura

    def atualizar_altura(self, no):
        no.altura = 1 + max(self.altura(no.esquerda),self.altura(no.direita))

    def fator_balanceamento(self, no):
        return self.altura(no.esquerda) - self.altura(no.direita)


    def rotacao_direita(self, y):
        self.rotacoes += 1
        x = y.esquerda
        t2 = x.direita
        x.direita = y
        y.esquerda = t2
        self.atualizar_altura(y)
        self.atualizar_altura(x)
        return x

    def rotacao_esquerda(self, x):
        self.rotacoes += 1
        y = x.direita
        t2 = y.esquerda
        y.esquerda = x
        x.direita = t2
        self.atualizar_altura(x)
        self.atualizar_altura(y)
        return y

    # INSERÇÃO

    def inserir(self, palavra, linha):
        self.raiz = self._inserir(self.raiz, palavra, linha)

    def _inserir(self, no,palavra, linha):
        if not no:
            return NO(palavra, linha)

        if palavra < no.palavra:
            no.esquerda = self._inserir(no.esquerda, palavra, linha)
        elif palavra > no.palavra:
            no.direita = self._inserir(no.direita, palavra, linha)
        else:
            if linha not in no.linhas:
                no.linhas.add(linha)
            else:
                self.total_descartadas += 1
            return no

        self.atualizar_altura(no)
        balance = self.fator_balanceamento(no)

        # Caso Esquerda-Esquerda
        if balance > 1 and palavra < no.esquerda.palavra:
            return self.rotacao_direita(no)

        # Caso Direita-Direita
        if balance < -1 and palavra > no.direita.palavra:
            return self.rotacao_esquerda(no)

        # Caso Esquerda-Direita
        if balance > 1 and palavra > no.esquerda.palavra:
            no.esquerda = self.rotacao_esquerda(no.esquerda)
            return self.rotacao_direita(no)

        # Caso Direita-Esquerda
        if balance < -1 and palavra < no.direita.palavra:
            no.direita = self.rotacao_direita(no.direita)
            return self.rotacao_esquerda(no)
        return no

    # REMOÇÃO
    def remover(self, palavra, linha):
        self.raiz = self._remover(self.raiz, palavra, linha)

    def _remover(self, no, palavra, linha):
        if not no:
            return no

        if palavra < no.palavra:
            no.esquerda = self._remover(no.esquerda, palavra, linha)
        elif palavra > no.palavra:
            no.direita = self._remover(no.direita, palavra, linha)
        else:
            if linha in no.linhas:
                no.linhas.remove(linha)

            if len(no.linhas) == 0:
                if not no.esquerda:
                    return no.direita
                elif not no.direita:
                    return no.esquerda

        return no

    # Busca com Medidor de Equilibrio

    def buscar(self, palavra):
        no = self._buscar(self.raiz, palavra)
        if not no:
            return -1
        esquerda = self.contar_nos(no.esquerda)
        direita = self.contar_nos(no.direita)
        me = esquerda - direita
        if me == 0:
            return 0
        else:
            print("Medidor de Equilíbrio (ME):", me)
            return 1

    def _buscar(self, no, palavra):
        if not no:
            return None
        if palavra == no.palavra:
            return no
        elif palavra < no.palavra:
            return self._buscar(no.esquerda, palavra)
        else:
            return self._buscar(no.direita, palavra)

    def contar_nos(self, no):
        if not no:
            return 0
        return 1 + self.contar_nos(no.esquerda) + self.contar_nos(no.direita)


    # Busca por prefixo

    def busca_prefixo(self, prefixo):
        resultado = []
        self._busca_prefixo(self.raiz, prefixo, resultado)
        return resultado

    def _busca_prefixo(self, no, prefixo, resultado):
        if not no:
            return
        if no.palavra.startswith(prefixo):
            resultado.append(no.palavra)
        self._busca_prefixo(no.esquerda, prefixo, resultado)
        self._busca_prefixo(no.direita, prefixo, resultado)


    # Palavra mais frequente

    def palavra_mais_frequente(self):
        return self._mais_frequente(self.raiz, ("", 0))[0]

    def _mais_frequente(self, no, atual):
        if not no:
            return atual
        if len(no.linhas) > atual[1]:
            atual = (no.palavra, len(no.linhas))
        atual = self._mais_frequente(no.esquerda, atual)
        atual = self._mais_frequente(no.direita, atual)
        return atual


    # Impressao ordem alfabetica

    def imprimir_indice(self, arquivo_saida):
        with open(arquivo_saida, "w", encoding="utf-8") as f:
            self._inorder(self.raiz, f)
            f.write("\n")
            f.write(f"Número total de palavras: {self.total_palavras}\n")
            f.write(f"Número de palavras distintas: {self.contar_nos(self.raiz)}\n")
            f.write(f"Número de palavras descartadas: {self.total_descartadas}\n")
            f.write(f"Tempo de construção: {self.tempo_construcao:.4f}s\n")
            f.write(f"Total de rotações executadas: {self.rotacoes}\n")


    def _inorder(self, no, f):
        if not no:
            return
        self._inorder(no.esquerda, f)
        linhas = ",".join(str(l) for l in sorted(no.linhas))
        f.write(f"{no.palavra} {linhas}\n")
        self._inorder(no.direita, f)
