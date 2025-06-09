# projeto-pratico
import os

# Lista para armazenar os usuários
usuarios = []

def limpar_tela():
    """Limpa a tela do terminal (opcional)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    """Exibe o menu principal."""
    print("\n===== MENU PRINCIPAL =====")
    print("1. Cadastrar usuário")
    print("2. Listar usuários")
    print("3. Buscar usuário por nome")
    print("4. Sair")

def cadastrar_usuario():
    """Cadastra um novo usuário após validações."""
    nome = input("Digite o nome do usuário: ").strip()
    idade = input("Digite a idade do usuário: ").strip()

    if not nome:
        print("❌ Nome não pode estar vazio.")
        return

    if not idade.isdigit() or int(idade) <= 0:
        print("❌ Idade deve ser um número inteiro positivo.")
        return

    usuarios.append({"nome": nome, "idade": int(idade)})
    print(f"✅ Usuário '{nome}' cadastrado com sucesso!")

def listar_usuarios():
    """Exibe todos os usuários cadastrados."""
    if not usuarios:
        print("⚠️ Nenhum usuário cadastrado.")
        return

    print("\n--- Lista de Usuários ---")
    for i, user in enumerate(usuarios, start=1):
        print(f"{i}. Nome: {user['nome']}, Idade: {user['idade']}")

def buscar_usuario():
    """Busca usuários por nome (parcial ou total, sem diferenciar maiúsculas)."""
    nome_busca = input("Digite o nome para buscar: ").strip().lower()

    if not nome_busca:
        print("❌ Nome para busca não pode estar vazio.")
        return

    encontrados = [u for u in usuarios if nome_busca in u['nome'].lower()]

    if encontrados:
        print("\n--- Usuário(s) Encontrado(s) ---")
        for user in encontrados:
            print(f"Nome: {user['nome']}, Idade: {user['idade']}")
    else:
        print("🔍 Nenhum usuário encontrado com esse nome.")

def executar_menu():
    """Executa o menu em loop até o usuário escolher sair."""
    while True:
        menu()
        escolha = input("Escolha uma opção (1-4): ").strip()

        if escolha == "1":
            cadastrar_usuario()
        elif escolha == "2":
            listar_usuarios()
        elif escolha == "3":
            buscar_usuario()
        elif escolha == "4":
            print("👋 Saindo do sistema. Até logo!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

# Inicia o programa
if __name__ == "__main__":
    executar_menu()

