import os
import sys

try:
    from src.padroniza_nomes_imgs import organizar_fotos
except ImportError:
    sys.exit(1)


try:
    from src.def_usuarios import capturar_da_webcam
except ImportError:
    sys.exit(1)

def exibir_menu():
    print("\n" + "="*45)
    print("   SISTEMA DE PREPARAÇÃO DE BANCO DE DADOS   ")
    print("="*45)
    print("[1] Capturar fotos em tempo real via WEBCAM")
    print("[2] Importar e renomear fotos de uma PASTA")
    print("[3] Sair do programa")
    print("="*45)

def pipeline_principal():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1, 2 ou 3): ").strip()

        if opcao == "1":
            print("\n--- Iniciando Módulo de Captura via Webcam ---")
            
            capturar_da_webcam()
            break

        elif opcao == "2":
            print("\n--- Iniciando Módulo de Organização de Pasta ---")
            
            pasta_origem = input("Digite o nome ou caminho da pasta de origem (Ex: minhas_fotos_originais): ").strip()
            
            if not pasta_origem:
                pasta_origem = "minhas_fotos_originais" # Valor padrão caso aperte Enter
                
            try:
                id_usuario = int(input("Digite o ID para este usuário (Padrão: 1): ") or 1)
            except ValueError:
                print("ID inválido. Usando ID padrão = 1.")
                id_usuario = 1
                
            organizar_fotos(pasta_origem, id_usuario)
            break

        elif opcao == "3":
            print("\nPrograma encerrado.")
            break
        else:
            print("\nOpção inválida! Por favor, escolha 1, 2 ou 3.")

if __name__ == "__main__":
    pipeline_principal()
