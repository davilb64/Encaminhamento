import os
import shutil

pasta_origem = r'I:\Meu Drive\COMERCIAL\SAC\CONTRATOS DIGITALIZADOS NOVO\À ORGANIZAR'
pasta_destino = r'C:\Users\Adm\Desktop\teste'  # Substitua pelo caminho da pasta de destino

# Função para extrair o número do nome do arquivo
def extrair_numero(nome_arquivo):
    partes = nome_arquivo.split()
    for parte in partes:
        if parte.isdigit():
            return parte

# Percorre os arquivos na pasta de origem
for _, _, arquivos in os.walk(pasta_origem):
    for arquivo in arquivos:
        if any(x in arquivo for x in ["CONT", "DEV", "REM", "TROCA"]):
            numero = extrair_numero(arquivo)
            if numero:
                pasta_numero = os.path.join(pasta_destino, numero)
                try:
                    if not os.path.exists(pasta_numero):
                        os.makedirs(pasta_numero)
                    shutil.move(os.path.join(pasta_origem, arquivo), os.path.join(pasta_numero, arquivo))
                    print(f"Arquivo '{arquivo}' movido para '{pasta_numero}'")
                except Exception as e:
                    print(f"Erro ao mover o arquivo '{arquivo}': {str(e)}")

