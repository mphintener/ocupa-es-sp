import re
import csv
from datetime import datetime

def extrair_dados_vaga_dinamica(texto_bruto, url_fonte):
    # 1. Filtro Soberano: Busca CEP na faixa da Capital (01000 a 08499)
    padrao_cep = r'0[1-8][0-9]{3}-?[0-9]{3}'
    cep_encontrado = re.search(padrao_cep, texto_bruto)
    
    if not cep_encontrado:
        return None # Ignora se não for SP-Capital

    # 2. Identificação de Característica (O que o trabalhador faz)
    # Busca verbos de ação e substantivos após palavras de impacto
    padrao_caracteristica = r'(?:para|vaga de|atuação em)\s+([^,.;]{10,50})'
    match_carac = re.search(padrao_caracteristica, texto_bruto, re.IGNORECASE)
    caracteristica = match_carac.group(1).strip() if match_carac else "Atividade não especificada"

    # 3. Identificação de Salário (Padrão Monetário)
    padrao_salario = r'R\$\s?(\d{1,3}(\.\d{3})*(,\d{2})?)'
    match_salario = re.search(padrao_salario, texto_bruto)
    salario = match_salario.group(1).replace('.', '').replace(',', '.') if match_salario else "0.00"

    # 4. Identificação de Qualificação (Padrão de Instrução)
    padrao_qualif = r'(ensino\s\w+|curso\s\w+|técnico\s\w+|nr-\d{2}|cnh\s[a-e])'
    qualificacoes = re.findall(padrao_qualif, texto_bruto, re.IGNORECASE)

    return {
        "timestamp_captura": datetime.now().isoformat(),
        "id_origem": url_fonte.split('//')[-1].split('/')[0], # Extrai o domínio
        "caracteristica_bruta": caracteristica,
        "salario_ofertado": float(salario),
        "qualificacao_exigida": "; ".join(set(qualificacoes)) if qualificacoes else "Não informada",
        "setor_inferido": "Análise Pendente", # Pode ser refinado por metadados do site
        "cep_localizacao": cep_encontrado.group()
    }

# Exemplo de uso com o texto "sujo" da rua:
texto_exemplo = "Contratamos urgente para conferência de estoque e carga. Salário R$ 2.250,50. Exige NR-11 e Ensino Médio. Local: Jaraguá, CEP 02998-000"
vaga_processada = extrair_dados_vaga_dinamica(texto_exemplo, "https://logistica-sp.com.br/vagas")

print(vaga_processada)
