from .models import Quizz
import matplotlib.pyplot as plt

def informacao_sobre_utilizadores(objetos):
    dados = {}
    for quizz in objetos:
        dados[quizz.nome] = QuizzPontuacao(quizz)

    return dados

def desenha_grafico_resultados(objetos):
    # creating the dataset
    dados = informacao_sobre_utilizadores(objetos)

    pessoa = list(dados.keys())
    pontuacao = list(dados.values())

    figuraOutput = plt.figure(figsize=(5, 5))

    # creating the bar plot
    plt.bar(pessoa, pontuacao, color='green',
            width=0.9)

    plt.xlabel("Nome dos participantes")
    plt.ylabel("Pontuação")
    plt.title("Pontuação dos participantes!")
    plt.savefig('portfolio/static/portfolio/images/grafico_final.png')


def QuizzPontuacao(input):
    pontuacaoDaPessoa = 0

    if input.pergunta1 == 1991:
        pontuacaoDaPessoa += 4

    if input.pergunta2 == 1994:
        pontuacaoDaPessoa += 4

    if input.pergunta3 == 1989:
        pontuacaoDaPessoa += 4

    if input.pergunta4 == "framework":
        pontuacaoDaPessoa += 4

    if input.pergunta5 == 2005:
        pontuacaoDaPessoa += 4

    return pontuacaoDaPessoa
