import json
import os

# Função para salvar os dados no arquivo JSON
def salvar_dados(nome, cpf, email):
    # Cria o nome do arquivo com base no nome do usuário
    nome_arquivo = f"{nome.replace(' ', '_')}_dados.json"
    
    dados = {
        "nome": nome,
        "cpf": cpf,
        "email": email
    }
    
    # Salva os dados no arquivo JSON específico para o usuário
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo)
    print(f"Arquivo '{nome_arquivo}' criado com sucesso!")  # Mensagem de sucesso no terminal

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
