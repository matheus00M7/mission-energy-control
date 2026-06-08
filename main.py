from src.dados_simulados import modulos
from src.analisador import avaliar_modulo, gerar_resumo
from src.visualizacao import exibir_cabecalho, exibir_avaliacao, exibir_resumo


def main():
    exibir_cabecalho()

    avaliacoes = []

    for modulo in modulos:
        avaliacao = avaliar_modulo(modulo)
        avaliacoes.append(avaliacao)
        exibir_avaliacao(avaliacao)

    resumo = gerar_resumo(avaliacoes)
    exibir_resumo(resumo)


if __name__ == "__main__":
    main()