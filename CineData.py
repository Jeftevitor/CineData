import json, os


def coloca_filme():
    filmes = []
    
    try:
        q = int(input("Quantos filmes deseja adicionar aos favoritos? "))
        
        for i in range(q):
            print(f"\n--- Filme {i+1} ---")
            filme = input("Nome do filme: ")

            # validação do ano
            ano = input("Ano de lançamento (4 dígitos): ")
            while not (ano.isdigit() and len(ano) == 4):
                ano = input("Ano inválido. Digite novamente (4 dígitos): ")
            ano = int(ano)

            genero = input("Gênero: ")

            assistiu = int(input("Quantas vezes você assistiu este filme? "))
            if assistiu < 0:
                assistiu = 0

            avaliacao = float(input("Avalie este filme entre 0 e 10: "))
            if avaliacao > 10:
                avaliacao = 10
            elif avaliacao < 0:
                avaliacao = 0

            filme_dict = {
                "Filme": filme,
                "Ano": ano,
                "Gênero": genero,
                "Vezes que você assistiu": assistiu,
                "Avaliação": avaliacao
            }

            filmes.append(filme_dict)

        return filmes

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return filmes

# Lê JSON existente
if os.path.exists("fav.json"):
    with open("fav.json", "r", encoding="utf-8") as f:
                dados_existentes = json.load(f)
else:
    dados_existentes = []

# Menu
print("Olá, bem vindo ao CineData!\n")
while True:
    print("\n\n\n ----- Menu -----:")
    print("Opção 1. Adicionar filmes a sua lista de favoritos.")
    print("Opção 2. Buscar ou edtar um filme na sua lista de favoritos.")
    print("Opção 3. Mostrar Ranking de todos os filmes.")
    print("Opção 4. Sair.")

    opcao = str(input("Escolha uma opção! "))

    # Opção 1:
    if opcao == "1":
        novos_filmes = coloca_filme()

        # Verificar duplicados
        nomes_existentes = [item["Filme"] for item in dados_existentes]

        filmes_para_adicionar = []

        for filme in novos_filmes:
            if filme["Filme"] in nomes_existentes:
                print(f"O filme '{filme['Filme']}' já está salvo. Ignorando...")
            else:
                filmes_para_adicionar.append(filme)

        # Salvar apenas os novos filmes válidos
        if filmes_para_adicionar:
            dados_existentes.extend(filmes_para_adicionar)

            with open("fav.json", "w", encoding="utf-8") as f:
                json.dump(dados_existentes, f, indent=2, ensure_ascii=False)

            print("\nFilmes adicionados com sucesso!")
        else:
            print("\nNenhum novo filme foi adicionado.")


    # Lê JSON existente
        if os.path.exists("fav.json"):
            with open("fav.json", "r", encoding="utf-8") as f:
                dados_existentes = json.load(f)
        else:
            dados_existentes = []

    # Opção 2:
    elif opcao == "2":
            
        a = [i["Avaliação"] for i in dados_existentes]
        avaliado = sorted(a, reverse=True)

        r = [i["Vezes que você assistiu"] for i in dados_existentes]
        ranking = sorted(r, reverse=True)

        while True:
            filme_b = input("Digite o nome do filme que deseja procurar: ")

            filme_encontrado = None
            for item in dados_existentes:
                if item["Filme"].lower() == filme_b.lower():
                    filme_encontrado = item

            if not filme_encontrado:
                print("Filme não encontrado!\n")

            else:
                print("\nFilme encontrado:")
                print(filme_encontrado)

                # Ranking por avaliação
                pos_avaliado = avaliado.index(filme_encontrado["Avaliação"]) + 1
                print(f"\nO filme {filme_b} é o {pos_avaliado}° mais bem avaliado!")

                # Ranking por vezes assistido
                pos_assistido = ranking.index(filme_encontrado["Vezes que você assistiu"]) + 1
                print(f"O filme {filme_b} é o {pos_assistido}° mais assistido!\n")

                # Menu de edição
                edit = input("Deseja editar os dados do filme? (s/n): ").lower()

                while edit == "s":
                    print("\nO que deseja editar?")
                    print("1. Nome")
                    print("2. Ano")
                    print("3. Gênero")
                    print("4. Vezes que você assistiu")
                    print("5. Avaliação")
                    print("0. Sair da edição")

                    opcao_e = input("Escolha uma opção: ")

                    if opcao_e == "1":
                        novo = input("Novo nome: ")
                        filme_encontrado["Filme"] = novo

                    elif opcao_e == "2":
                        novo = input("Novo ano (4 dígitos): ")
                        while not (novo.isdigit() and len(novo) == 4):
                            novo = input("Ano inválido. Digite novamente (4 dígitos): ")
                        filme_encontrado["Ano"] = int(novo)

                    elif opcao_e == "3":
                        novo = input("Novo gênero: ")
                        filme_encontrado["Gênero"] = novo

                    elif opcao_e == "4":
                        novo = int(input("Nova quantidade: "))
                        if novo < filme_encontrado["Vezes que você assistiu"]:
                            print("Não é possível adicionar um número menor que o anterior.")
                        else:
                            filme_encontrado["Vezes que você assistiu"] = novo

                    elif opcao_e == "5":
                        novo = float(input("Nova avaliação (0 a 10): "))
                        novo = max(0, min(10, novo))  # limita entre 0 e 10
                        filme_encontrado["Avaliação"] = novo

                    elif opcao_e == "0":
                        break

                    else:
                        print("Opção inválida!")

                    print("\nFilme atualizado:")
                    print(filme_encontrado)

                    # Salva no JSON após cada alteração
                    with open("fav.json", "w", encoding="utf-8") as f:
                        json.dump(dados_existentes, f, indent=2, ensure_ascii=False)

                print("\nEdição finalizada.\n")

            continuar = input("Deseja continuar buscando ou editando filmes? (s/n): ").lower()
            if continuar == "n":
                print("Ok, paramos por aqui!")
                break
    
    # Opção 3:
    elif opcao == "3":
        avaliado = sorted([i["Avaliação"] for i in dados_existentes], reverse=True)
        ranking = sorted([i["Vezes que você assistiu"] for i in dados_existentes], reverse=True)

        for indice, filme in enumerate(dados_existentes, start=1):
            print(f"Filme {indice}: {filme['Filme']}\n")

            pos_avaliado = avaliado.index(filme["Avaliação"]) + 1
            print("Avaliação:")
            print(f"→ {filme['Filme']} é o {pos_avaliado}° mais bem avaliado!\n")

            pos_assistido = ranking.index(filme["Vezes que você assistiu"]) + 1
            print("Assistidos:")
            print(f"→ {filme['Filme']} é o {pos_assistido}° mais assistido!\n")
            print("Vezes assistidas:", filme["Vezes que você assistiu"])

            print("-" * 40)

        while True:
            print("\nOpção 1. Retornar ao menu")
            print("Opção 2. Inserir vezes assistidas a um filme")
            opcao_r = input("Escolha uma opção: ")

            if opcao_r == "1":
                break

            elif opcao_r == "2":
                filme_n = int(input("Qual o número do filme que deseja editar? "))
                filme_e = dados_existentes[filme_n - 1]

                print(f"\nVocê selecionou: {filme_e['Filme']}")
                novo = int(input("Digite a nova quantidade: "))

                if novo < filme_e["Vezes que você assistiu"]:
                    print("\nNão é possível colocar um número menor que o anterior.")
                else:
                    filme_e["Vezes que você assistiu"] = novo
                    print("\nQuantidade atualizada com sucesso!")

                    with open("fav.json", "w", encoding="utf-8") as f:
                        json.dump(dados_existentes, f, indent=2, ensure_ascii=False)

            else:
                print("Opção inválida. Tente novamente.")
 
    #Opção 4:
    elif opcao == "4":
        print("Espero que tenha aproveitado a experiência!")
        print("Até breve. Fechando o progama...")
        break

    else:
        print("Opção inválida. Tente novamente.")