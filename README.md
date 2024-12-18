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

![image](https://github.com/user-attachments/assets/642b51f2-4a30-4f74-b795-e5399c4c5517)


---

## **Estrutura da Solução**

## **Fontes de Dados**
As fontes de dados utilizadas são as seguintes:

- **API Yahoo Finance**: Dados financeiros.
- **CSV Cliente**: Dados cadastrais dos clientes.
- **CSV Componentes Nasdaq100**: Informações dos componentes do índice Nasdaq100.

---

## **Pipeline de Dados**
O pipeline segue a **Medallion Architecture**, estruturada em três camadas:

### **1. Camada Bronze (RAW)**
- **Objetivo**: Preservação dos dados brutos e originais.
- **Formato**: CSV armazenado no **Amazon S3**.
- **Job**: `Origem_RAW.py`
- **Características**:
  - Captura fiel dos dados.
  - Armazenamento seguro no formato bruto.

---

### **2. Camada Silver**
- **Objetivo**: Transformação, limpeza e consolidação dos dados.
- **Formato**: Dados convertidos para **Parquet**.
- **Job**: `RAW_TO_SLV.py`
- **Transformações Realizadas**:
  - Conversão de tipos e limpeza de dados.
  - **Junção** de tabelas de clientes, componentes e cotações.
  - Cálculo de métricas básicas:
    - `ValorTotalAtivo`
    - `PatrimonioTotal`

---

### **3. Camada Gold**
- **Objetivo**: Dados agregados e prontos para análises.
- **Formato**: Parquet, com **particionamento otimizado**.
- **Job**: `SLV_TO_GLD.py`
- **Características**:
  - Cálculo de métricas analíticas por cliente.
  - Adição de **metadados** para otimizar consultas (ex.: data, ano, mês).

---

## **Consumo de Dados**
Os dados refinados são consumidos e visualizados através das seguintes ferramentas:

- **Amazon Athena**: 
  - Permite **consultas SQL interativas** diretamente sobre os dados no **Amazon S3**.
  - Elimina a necessidade de provisionar infraestrutura fixa.

- **Amazon QuickSight**:
  - **Dashboards e visualizações interativas** baseadas nos dados consultados pelo Athena.
  - Facilita a entrega rápida de **insights acionáveis** para os usuários.

---

## **Ferramentas AWS**
A solução utiliza os seguintes serviços da AWS:

- **AWS Glue**: Pipeline ETL para transformação e processamento dos dados.
- **Amazon S3**: Armazenamento centralizado e escalável das camadas **Bronze**, **Silver** e **Gold**.
- **Amazon Athena**: Consultas ad-hoc e análises SQL diretamente no S3.
- **Amazon QuickSight**: Visualização dos dados em dashboards intuitivos.

---

## **Fluxo Geral**
O fluxo de dados segue as etapas abaixo:

1. **Ingestão de Dados**:
   - Dados são coletados de fontes externas (**API Yahoo Finance** e **arquivos CSV**).

2. **Processamento**:
   - **AWS Lambda** aciona o **AWS Glue** para realizar a transformação dos dados.
   - Dados são organizados em camadas de maturidade:
     - **Bronze**: Dados brutos.
     - **Silver**: Dados transformados e consolidados.
     - **Gold**: Dados agregados e prontos para análise.

3. **Armazenamento**:
   - Todas as camadas são armazenadas no **Amazon S3** em formatos otimizados.

4. **Consulta e Visualização**:
   - **Amazon Athena** realiza consultas diretas no S3.
   - **Amazon QuickSight** entrega **dashboards interativos** com análises finais.

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
