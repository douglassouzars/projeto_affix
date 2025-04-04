import json
import os

# Função para salvar os dados no arquivo JSON
def salvar_dados(nome, cpf, email):
    try:
        nome_arquivo = f"{nome.replace(' ', '_')}_dados.json"
        dados = {"nome": nome, "cpf": cpf, "email": email}
        
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4)  # Indentação para melhor leitura
        
        print(f"Arquivo '{nome_arquivo}' criado com sucesso!")  
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

# Função para carregar os dados do arquivo JSON
def carregar_dados(nome):
    nome_arquivo = f"{nome.replace(' ', '_')}_dados.json"
    
    if os.path.exists(nome_arquivo):
        # Carrega os dados do arquivo JSON
        with open(nome_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
        return dados
    else:
        # Caso o arquivo não exista, retorna None
        return None
