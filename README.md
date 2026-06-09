# Mission Energy Control

## Sobre o projeto

O **Mission Energy Control** é um sistema desenvolvido em Python para simular o monitoramento energético de uma missão espacial experimental.

O projeto tem como objetivo interpretar dados simulados de módulos operacionais de uma missão, analisando informações como energia, temperatura, comunicação e status dos sistemas. A partir desses dados, o sistema gera alertas automáticos e recomenda ações básicas para auxiliar na tomada de decisão em cenários normais, de atenção ou críticos.

Este projeto foi desenvolvido como parte da **Global Solution 2026.1 — Soluções em Energias Renováveis e Sustentáveis**, no curso de **Ciência da Computação**.

---

## Objetivo

Desenvolver uma solução computacional capaz de monitorar sistemas energéticos de uma missão espacial experimental, aplicando conceitos de programação, pensamento computacional, análise de dados simulados, geração de alertas e tomada de decisão automatizada.

O sistema busca representar, de forma simplificada, como um centro de controle poderia acompanhar o funcionamento de módulos essenciais de uma missão espacial, especialmente em relação ao uso de energia e à estabilidade operacional.

---

## Contexto da solução

Em missões espaciais, o controle de energia é um fator essencial para a segurança e continuidade da operação. Sistemas como painéis solares, baterias, comunicação, navegação e suporte à vida precisam ser constantemente monitorados.

Caso algum módulo apresente falha, baixa energia, superaquecimento ou perda de comunicação, o sistema deve identificar rapidamente o problema e sugerir ações corretivas.

O **Mission Energy Control** simula esse cenário, permitindo a análise de módulos operacionais e a geração de alertas automáticos conforme os dados recebidos.

---

## Funcionalidades

* Monitoramento de dados simulados da missão;
* Análise de energia dos módulos;
* Verificação de temperatura;
* Verificação do status de comunicação;
* Identificação de módulos em situação normal, atenção ou crítica;
* Geração automática de alertas;
* Recomendação de ações básicas para tomada de decisão;
* Exibição organizada dos dados no terminal;
* Resumo final da situação geral da missão.

---

## Lógica de análise

O sistema avalia os dados de cada módulo da missão e classifica sua situação de acordo com regras lógicas simples.

Exemplos de critérios utilizados:

* Energia muito baixa pode gerar alerta crítico;
* Temperatura elevada pode indicar risco operacional;
* Falha de comunicação pode comprometer o controle da missão;
* Módulos essenciais recebem maior prioridade na análise;
* Situações críticas geram recomendações automáticas.

Com isso, o sistema simula uma tomada de decisão básica diante de possíveis falhas em uma missão espacial.

---

## Dados monitorados

Os principais dados simulados pelo sistema são:

* Nome do módulo;
* Nível de energia;
* Temperatura;
* Status de comunicação;
* Status operacional;
* Tipo de módulo;
* Nível de criticidade;
* Recomendação de ação.

---

## Estrutura do projeto

```bash
mission-energy-control/
│
├── main.py
├── README.md
├── .gitignore
│
└── src/
    ├── analisador.py
    ├── dados_simulados.py
    └── visualizacao.py
```

### Descrição dos arquivos

* **main.py**
  Arquivo principal responsável por iniciar a execução do sistema.

* **src/dados_simulados.py**
  Contém os dados simulados dos módulos da missão espacial.

* **src/analisador.py**
  Contém a lógica de análise dos dados, geração de alertas e recomendações.

* **src/visualizacao.py**
  Responsável por exibir as informações da missão de forma organizada no terminal.

* **.gitignore**
  Arquivo usado para evitar o envio de pastas e arquivos desnecessários ao GitHub, como ambiente virtual, cache do Python e configurações da IDE.

---

## Tecnologias utilizadas

* Python 
* Git
* GitHub
* PyCharm

---

## Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/matheus00M7/mission-energy-control.git
```

### 2. Acesse a pasta do projeto

```bash
cd mission-energy-control
```

### 3. Execute o arquivo principal

```bash
python main.py
```

Ou, dependendo da configuração do seu computador:

```bash
python3 main.py
```

---

## Exemplo de funcionamento

Ao executar o projeto, o sistema apresenta os módulos da missão, analisa suas condições operacionais e exibe alertas conforme a situação identificada.

Exemplo de análise:

```text
Módulo: Painel Solar
Energia: 76%
Temperatura: 35°C
Comunicação: Estável
Status: Operacional
Situação: Normal

Módulo: Bateria Principal
Energia: 18%
Temperatura: 72°C
Comunicação: Instável
Status: Atenção
Situação: Crítico
Ação recomendada: Reduzir consumo energético e priorizar módulos essenciais.
```

---

## Relação com o tema da Global Solution

O projeto está relacionado ao tema **Soluções em Energias Renováveis e Sustentáveis**, pois trabalha com o monitoramento energético de uma missão espacial experimental.

A solução simula a análise de sistemas que dependem de energia para funcionar corretamente, como painéis solares, baterias e módulos operacionais. Dessa forma, o sistema contribui para a ideia de uso eficiente da energia, identificação de falhas e tomada de decisão em ambientes críticos.

---

## Vídeo de apresentação

Link do vídeo no YouTube:

```text
COLOCAR AQUI O LINK DO VÍDEO NÃO LISTADO
```

---

## Integrantes

Matheus Martins Lacerda — RM: 570843

Roberson Roguero Luiz Junior — RM: 573031

---

## Disciplina

Global Solution 2026.1
Soluções em Energias Renováveis e Sustentáveis
Ciência da Computação — FIAP

---

## Status do projeto

Projeto em desenvolvimento para entrega acadêmica, contendo uma simulação funcional de monitoramento energético aplicado a uma missão espacial experimental.
