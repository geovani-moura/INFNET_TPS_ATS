from os.path import dirname, join
import os
import glob


def run(files):
    """
    Run all scripts
    """
    for pyfile in files:
        print(f"Executando {pyfile} ...")
        print()
        try:
            os.system(f"python {pyfile}")
        except Exception as e:
            print(f"Erro ao executar o script {pyfile}: {e}")
        print()
        print("#" * 30)


print("Qual questão você gostaria de executar?")
url = os.path.join(os.path.dirname(__file__), "questoes")
files = sorted(os.listdir(url))

# Exibe a lista de arquivos e suas opções
for idx, file in enumerate(files):
    print(f"{idx + 1} - {file}")

print(f"{len(files) + 1} - Executar todos")

option = input("Escolha uma opção: ")

try:
    option = int(option)
    if 1 <= option <= len(files):
        run([files[option - 1]])  # Ajustado para garantir a execução correta
    elif option == len(files) + 1:
        run(files)  # Executa todos os arquivos
    else:
        print("Opção Inválida")
except ValueError:
    print("Entrada inválida. Por favor, insira um número.")
