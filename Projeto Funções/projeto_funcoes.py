from tabulate import tabulate

tarefas = []

def adicionar_tarefa():
    nome = input("Nome da tarefa: ")
    descricao = input("Descrição da tarefa: ")
    prioridade = input("Prioridade da tarefa (alta, média, baixa): ")
    categoria = input("Categoria da tarefa: ")
    tarefa = {"nome": nome, "descricao": descricao, "prioridade": prioridade, "categoria": categoria, "concluida": False}
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso.")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    headers = ["Nome", "Descrição", "Prioridade", "Categoria", "Concluída"]
    rows = [[tarefa["nome"], tarefa["descricao"], tarefa["prioridade"], tarefa["categoria"], "Sim" if tarefa["concluida"] else "Não"] for tarefa in tarefas]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

def marcar_como_concluida():
    nome_tarefa = input("Nome da tarefa a ser marcada como concluída: ")
    for tarefa in tarefas:
        if tarefa["nome"] == nome_tarefa:
            tarefa["concluida"] = True
            print(f"Tarefa '{nome_tarefa}' marcada como concluída.")
            return
    print(f"Tarefa '{nome_tarefa}' não encontrada.")

def exibir_por_prioridade():
    prioridade = input("Prioridade a ser filtrada (alta, média, baixa): ")
    tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa["prioridade"] == prioridade]
    if not tarefas_filtradas:
        print(f"Nenhuma tarefa encontrada com prioridade '{prioridade}'.")
        return
    headers = ["Nome", "Descrição", "Categoria", "Concluída"]
    rows = [[tarefa["nome"], tarefa["descricao"], tarefa["categoria"], "Sim" if tarefa["concluida"] else "Não"] for tarefa in tarefas_filtradas]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

def exibir_por_categoria():
    categoria = input("Categoria a ser filtrada: ")
    tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa["categoria"] == categoria]
    if not tarefas_filtradas:
        print(f"Nenhuma tarefa encontrada na categoria '{categoria}'.")
        return
    headers = ["Nome", "Descrição", "Prioridade", "Concluída"]
    rows = [[tarefa["nome"], tarefa["descricao"], tarefa["prioridade"], "Sim" if tarefa["concluida"] else "Não"] for tarefa in tarefas_filtradas]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

def menu():
    while True:
        print("\n=== Menu de Tarefas ===")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Exibir Tarefas por Prioridade")
        print("5. Exibir Tarefas por Categoria")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            marcar_como_concluida()
        elif opcao == "4":
            exibir_por_prioridade()
        elif opcao == "5":
            exibir_por_categoria()
        elif opcao == "6":
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    menu()