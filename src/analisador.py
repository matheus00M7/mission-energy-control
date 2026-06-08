def analisar_energia(energia):
    if energia < 30:
        return {
            "nivel": "CRÍTICO",
            "mensagem": "Energia muito baixa.",
            "acao": "Ativar modo economia e desligar módulos não essenciais."
        }
    elif energia < 60:
        return {
            "nivel": "ATENÇÃO",
            "mensagem": "Energia abaixo do ideal.",
            "acao": "Reduzir consumo energético e monitorar bateria."
        }
    else:
        return {
            "nivel": "NORMAL",
            "mensagem": "Energia em nível adequado.",
            "acao": "Manter operação normal."
        }


def analisar_temperatura(temperatura):
    if temperatura > 65:
        return {
            "nivel": "CRÍTICO",
            "mensagem": "Temperatura muito elevada.",
            "acao": "Reduzir carga dos sistemas e verificar resfriamento."
        }
    elif temperatura > 40:
        return {
            "nivel": "ATENÇÃO",
            "mensagem": "Temperatura acima do ideal.",
            "acao": "Monitorar aquecimento do módulo."
        }
    else:
        return {
            "nivel": "NORMAL",
            "mensagem": "Temperatura em nível adequado.",
            "acao": "Manter operação normal."
        }


def analisar_comunicacao(comunicacao):
    if comunicacao < 40:
        return {
            "nivel": "CRÍTICO",
            "mensagem": "Comunicação crítica.",
            "acao": "Priorizar canal principal de comunicação."
        }
    elif comunicacao < 70:
        return {
            "nivel": "ATENÇÃO",
            "mensagem": "Comunicação instável.",
            "acao": "Reforçar sinal e monitorar conexão."
        }
    else:
        return {
            "nivel": "NORMAL",
            "mensagem": "Comunicação estável.",
            "acao": "Manter operação normal."
        }


def definir_status_modulo(analises):
    niveis = [
        analises["energia"]["nivel"],
        analises["temperatura"]["nivel"],
        analises["comunicacao"]["nivel"]
    ]

    if "CRÍTICO" in niveis:
        return "CRÍTICO"
    elif "ATENÇÃO" in niveis:
        return "ATENÇÃO"
    else:
        return "NORMAL"


def avaliar_modulo(modulo):
    analises = {
        "energia": analisar_energia(modulo["energia"]),
        "temperatura": analisar_temperatura(modulo["temperatura"]),
        "comunicacao": analisar_comunicacao(modulo["comunicacao"])
    }

    status_geral = definir_status_modulo(analises)

    return {
        "modulo": modulo,
        "analises": analises,
        "status_geral": status_geral
    }


def gerar_resumo(avaliacoes):
    total_modulos = len(avaliacoes)

    modulos_criticos = 0
    modulos_atencao = 0
    modulos_normais = 0

    for avaliacao in avaliacoes:
        if avaliacao["status_geral"] == "CRÍTICO":
            modulos_criticos += 1
        elif avaliacao["status_geral"] == "ATENÇÃO":
            modulos_atencao += 1
        else:
            modulos_normais += 1

    if modulos_criticos > 0:
        status_missao = "CRÍTICO"
        acao_principal = "Priorizar economia de energia e proteger módulos essenciais."
    elif modulos_atencao > 0:
        status_missao = "ATENÇÃO"
        acao_principal = "Monitorar módulos instáveis e reduzir consumo preventivamente."
    else:
        status_missao = "NORMAL"
        acao_principal = "Manter operação normal."

    return {
        "total_modulos": total_modulos,
        "modulos_criticos": modulos_criticos,
        "modulos_atencao": modulos_atencao,
        "modulos_normais": modulos_normais,
        "status_missao": status_missao,
        "acao_principal": acao_principal
    }