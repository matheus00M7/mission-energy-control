def exibir_cabecalho():
    print("=" * 60)
    print("MISSION ENERGY CONTROL")
    print("Monitoramento inteligente de sistemas energéticos espaciais")
    print("=" * 60)
    print()


def exibir_avaliacao(avaliacao):
    modulo = avaliacao["modulo"]
    analises = avaliacao["analises"]

    print("-" * 60)
    print(f"Módulo: {modulo['nome']}")
    print(f"Status informado: {modulo['status']}")
    print()
    print(f"Energia: {modulo['energia']}%")
    print(f"Temperatura: {modulo['temperatura']}°C")
    print(f"Comunicação: {modulo['comunicacao']}%")
    print()
    print(f"Alerta energia: {analises['energia']['nivel']}")
    print(f"Mensagem: {analises['energia']['mensagem']}")
    print(f"Ação: {analises['energia']['acao']}")
    print()
    print(f"Alerta temperatura: {analises['temperatura']['nivel']}")
    print(f"Mensagem: {analises['temperatura']['mensagem']}")
    print(f"Ação: {analises['temperatura']['acao']}")
    print()
    print(f"Alerta comunicação: {analises['comunicacao']['nivel']}")
    print(f"Mensagem: {analises['comunicacao']['mensagem']}")
    print(f"Ação: {analises['comunicacao']['acao']}")
    print()
    print(f"STATUS GERAL DO MÓDULO: {avaliacao['status_geral']}")
    print("-" * 60)
    print()


def exibir_resumo(resumo):
    print("=" * 60)
    print("RESUMO FINAL DA MISSÃO")
    print("=" * 60)
    print(f"Total de módulos analisados: {resumo['total_modulos']}")
    print(f"Módulos críticos: {resumo['modulos_criticos']}")
    print(f"Módulos em atenção: {resumo['modulos_atencao']}")
    print(f"Módulos normais: {resumo['modulos_normais']}")
    print()
    print(f"STATUS GERAL DA MISSÃO: {resumo['status_missao']}")
    print(f"Ação principal recomendada: {resumo['acao_principal']}")
    print("=" * 60)