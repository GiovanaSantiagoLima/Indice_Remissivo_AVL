# Índice Remissivo com Árvore AVL 🌳📖

Este projeto implementa um sistema de índice remissivo automatizado para documentos de texto, desenvolvido em Python. Utilizando a estrutura de dados de uma Árvore Binária de Busca Balanceada (AVL), o sistema processa textos selecionados de Fernando Pessoa, extraindo as palavras, mapeando as linhas onde ocorrem e garantindo alta eficiência em operações de busca e ordenação.

## 👥 Autores
* **Giovana Santiago**
* **Thalita Judice**

---

## 📌 Introdução

**Compreensão do Problema:**
O objetivo principal foi mapear a ocorrência de palavras em um documento texto, desconsiderando diferenças entre maiúsculas e minúsculas, além de pontuações. O sistema precisava registrar as linhas em que cada palavra aparece, sem duplicidade de linhas para o mesmo termo. Para atender aos requisitos de desempenho em um texto longo, foi necessário implementar um sistema de balanceamento automático.

**Desenho da Solução e Estruturas de Dados:**
A solução central baseia-se em uma **Árvore AVL**. Por ser uma árvore de busca auto-balanceada, ela mantém sua altura mínima, garantindo eficiência nas operações (complexidade $O(\log n)$). Cada nó armazena a palavra (chave) e um conjunto (`set`) com os números das linhas de ocorrência.

## 📂 Estrutura do Projeto

O código foi modularizado nos seguintes arquivos:

* **`main.py`**: Arquivo principal. Orquestra a execução, inicializa a árvore, chama a leitura do texto e gera os resultados.
* **`arvore_avl.py`**: Contém a classe `AVL` com a lógica de inserção, remoção, rotações (direita/esquerda), busca, cálculo de fator de balanceamento e travessia.
* **`no_avl.py`**: Define a classe `NO`, representando cada nodo da árvore (contém a palavra, o conjunto de linhas e ponteiros para esquerda/direita).
* **`leitura_texto.py`**: Módulo responsável por abrir o arquivo `.txt`, limpar a pontuação das palavras e inseri-las na árvore.
* **`texto_origem.txt`**: Arquivo de entrada contendo a obra de Fernando Pessoa.
* **`indice_saida.txt`**: (Gerado automaticamente) Arquivo de saída contendo o índice remissivo final e as estatísticas.

---

## 🚀 Como Executar

Certifique-se de ter o **Python 3.x** instalado.

1.  Clone este repositório ou baixe os arquivos para uma pasta local.
2.  Abra o terminal na pasta do projeto.
3.  Execute o comando:

```bash
python main.py