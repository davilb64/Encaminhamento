import os
import shutil
import re

pasta_origem = r'I:\Meu Drive\COMERCIAL\SAC\CONTRATOS DIGITALIZADOS NOVO\À ORGANIZAR'
pasta_destino = r'I:\Meu Drive\COMERCIAL\SAC\CONTRATOS DIGITALIZADOS NOVO\temp'  # Substitua pelo caminho da pasta de destino

# Função para extrair o número do nome do arquivo usando expressões regulares
def extrair_numero(nome_arquivo):
    numero = re.search(r'\d+', nome_arquivo)
    if numero:
        return numero.group()
    else:
        return None

# Percorre os arquivos na pasta de origem
for _, _, arquivos in os.walk(pasta_origem):
    for arquivo in arquivos:
        numero = extrair_numero(arquivo)
        if numero:
            pasta_numero = os.path.join(pasta_destino, numero)
            try:
                if not os.path.exists(pasta_numero):
                    os.makedirs(pasta_numero)
                shutil.move(os.path.join(pasta_origem, arquivo), pasta_numero)
                print(f"Arquivo '{arquivo}' movido para '{pasta_numero}'")
            except Exception as e:
                print(f"Erro ao mover o arquivo '{arquivo}': {str(e)}")
