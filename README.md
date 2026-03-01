# Ocupações SP | Rastreamento Dinâmico de Vagas de Trabalho

Este módulo faz parte do ecossistema **Calculadora do Trecho** e atua como um monitor independente de ofertas de trabalho na Capital de São Paulo (CEP 01000-08499).

## 🚀 Lógica de Funcionamento (Non-Rigid Syntax)
Diferente de agregadores governamentais ou sites de emprego tradicionais, este rastreador não utiliza dicionários estáticos (CBO) ou listas de cargos engessadas. Ele opera via **Reconhecimento de Estrutura de Oferta**:

1. **Descoberta Autônoma:** O robô identifica padrões de "Troca Econômica" (Oferecemos R$ + Exigimos X) em sites de empresas e portais privados.
2. **Extração Qualitativa:** Isola a *Característica Bruta* da vaga (o que o trabalhador fará de fato) em vez de apenas o nome do cargo.
3. **Ancoragem Territorial:** Toda vaga é obrigatoriamente vinculada a um CEP da Capital para análise de clusters.

## 📊 Estrutura do Dado (JSON/CSV)
O output do rastreador alimenta a página **Ocupações SP** e o **NotebookLM** com os seguintes atributos:
- `id_origem`: Empresa ofertante (extração direta).
- `caracteristica_bruta`: Descrição real da função.
- `salario_ofertado`: Valor numérico isolado.
- `qualificacao_exigida`: Requisitos técnicos (Cursos, NR, Escolaridade).
- `setor_inferido`: Atividade econômica detectada.
- `cep_localizacao`: Âncora geográfica (01-08).

## 🎨 Identidade Visual (Dashboard)
O front-end segue o padrão de alto contraste:
- **Fundo:** Preto
- **Dados Principais:** Amarelo
- **Alertas de Qualificação:** Vermelho
---
**Objetivo:** Mapear o descompasso entre a qualificação oferecida pelas unidades escolares locais e a demanda real das empresas em cada cluster da cidade.
Roadmap: Ocupações SP (Evolução 2026)
Este roteiro deve ser colocado no final do seu README.md. Ele separa o que já temos ("Motor de Extração") do que a Página Ocupações SP vai se tornar.

Fase 1: Extração Qualitativa (Concluído)
[x] Criar motor de reconhecimento de estrutura (SDR-SP).

[x] Filtragem por faixas de CEP da Capital (01-08).

[x] Extração de Característica Bruta, Salário e Qualificação.

Fase 2: Geointeligência Educacional (Em Breve)
[ ] Mapeamento dinâmico de unidades escolares (ETECs/SENAI) por proximidade de CEP.

[ ] Cálculo automático de "Gap de Qualificação" (Vagas vs. Cursos locais).

[ ] Integração com a Calculadora do Trecho para medir o impacto do deslocamento no salário real.

Fase 3: Dashboard de Visualização (Escopo)
[ ] Interface em alto contraste (Preto, Amarelo e Vermelho).

[ ] Filtro por "Verbos de Ação" (Ex: Operar, Analisar, Conferir).

[ ] Exportação direta de relatórios para o NotebookLM.

🚩 Primeira Issue: #001 - Implementação da Camada de Inferência de Setores
No GitHub, as "Issues" mostram os desafios técnicos que você está resolvendo. Crie esta primeira tarefa:

Título: [Melhoria] Implementar Classificação Dinâmica de Setores de Atividade

Descrição:

"Atualmente, o campo setor_inferido está como 'Análise Pendente'. Precisamos evoluir o script para que ele identifique o setor econômico (Logística, Indústria, Varejo, Serviços) com base na densidade de termos extraídos da caracteristica_bruta e dos metadados da empresa ofertante, sem depender de uma lista estática de palavras-chave."

💼 A Narrativa de Especialista
Com esse Roadmap e a Issue aberta, você consolida a sua fala:

"O projeto Ocupações SP não é uma ferramenta estática. Ele está em constante evolução para mapear não só a vaga, mas o ecossistema ao redor dela: onde o trabalhador se qualifica e quanto do salário dele sobra após o 'trecho'."
