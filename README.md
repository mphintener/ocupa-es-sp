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
