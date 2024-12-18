# :rocket: XPTO Data Consulting :rocket:

## Grupo

| Nome               | RA |
| -------------      | ---------- |
| Aline Couto        | 10206399   |
| Carolina Attili    | 10369043   |
| Cristian Barros    | 10444616   |
| Davi Santos        | 10444890   |


---
## Quem somos
A XPTO Consultoria de Dados é uma empresa especializada em transformar dados em insights estratégicos para grandes organizações. Ajudamos nossos clientes a otimizar processos, melhorar a tomada de decisões e impulsionar a inovação. 

---

## Definição do problema
  Corretores de investimentos com problemas de atualização e acompanhamento de valores de carteira dos clientes 

---

## Objetivo
O problema enfrentado por corretores de investimentos é a dificuldade em manter os valores das carteiras dos clientes sempre atualizados em tempo real. Isso ocorre devido a desafios na integração e atualização de dados financeiros, como variações diárias de preços de ativos, mudanças em índices de mercado e taxas de câmbio. A falta de uma ferramenta eficiente e automatizada para esse processo resulta em informações desatualizadas, o que compromete a precisão das recomendações de investimento e a tomada de decisões pelos clientes. Esse problema pode afetar a confiança do cliente e a qualidade do serviço prestado, tornando essencial a implementação de soluções tecnológicas que garantam a atualização contínua e precisa das carteiras.

---

## Proposta de Solução


![solution](https://github.com/user-attachments/assets/3e00ffb6-f72d-4b5c-a708-356c311e785c)


Este diagrama descreve uma solução de processamento e análise de dados baseada em serviços da AWS, organizados em duas camadas: Batch Layer (camada de processamento em lote) e Speed Layer (camada de baixa latência). A seguir, uma descrição detalhada.

Batch Layer (Camada de Processamento em Lote):
Fontes de Dados:

API Yahoo Finance: Fonte externa para aquisição de dados financeiros.
CSV Cliente: Arquivos CSV contendo dados enviados pelos clientes.


AWS Lambda:
Responsável por orquestrar a ingestão de dados. Invoca o serviço AWS Glue para processar e transformar os dados recebidos.

AWS Glue:
Realiza a transformação e o tratamento dos dados. É configurado para organizar os dados em diferentes níveis:
Bronze: Dados brutos armazenados em formato CSV no S3.
Silver: Dados parcialmente processados e transformados em formato Parquet, no S3.
Gold: Dados finais refinados também armazenados em formato Parquet, no S3.

Amazon Athena:
Serviço de consulta interativa que permite explorar diretamente os dados armazenados no S3. Útil para relatórios ou consultas ad-hoc sem necessidade de carregamento de dados para outro sistema.

Fluxo Geral:
Dados são coletados de fontes externas (API e CSV).
Lambda e Glue transformam os dados em diferentes camadas de maturidade (Bronze, Silver, Gold).
Dados refinados são armazenados no Athena para análises detalhadas.
As análises finais são disponibilizadas para os usuários em dashboards no QuickSight.

---
## Gestão do projeto 

Utilizamos o Trello para fazer a organização e distribuição das tarefas do projeto por sprints. 
https://trello.com/b/dCeSl1NL/mba-hands-on-eng-dados


### Sprint 1 
- [X] Definição do problema
- [X] Escolha da base de dados
- [X] Desenho de arquitetura
- [X] Configuração do Streamlit
- [X] Escolha do Stack de Ferramentas

### Sprint 2 
- [X] Criação do kanban(tarefas e responsáveis)
- [X] Modelagem das camadas de dados

### Sprint 3 
- [X] Definição MVP
- [X] Planner MVP
- [X] Levantamento de requisitos
- [X] Preparação ambiente

### Sprint 4
- [X] Análise e Design
- [X] Configuração
- [X] Desenvolvimento
- [X] Calculadora de Custos
- [X] Teste e validação
- [X] Apresentação Final


### Calculadora de custo:
Foi realizada a simulação de custos para manter o MVP deste projeto, considerando os recursos da AWS utilizados:
Lambda, Glue, Athena 


### Critério de Avaliação:
- Proposição para mercado prático
- Detalhamento técnico Arquitetura
- Demonstração Funcional MVP
- Documentação Entregue, Git Hub
- Utilização Ferramentas Big Data
