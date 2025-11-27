import json, os

def coloca_filme():
    filmes = []
    q = int(input("Quantos filmes deseja adicionar aos favoritos? "))

    for i in range(q):
        print(f"\n--- Filme {i+1} ---")
        filme = input("Nome do filme: ")
        ano = int(input("Ano de lançamento: "))
        genero = input("Gênero: ")
        avaliacao = float(input("Avalie este filme entre 0 e 10: "))

        if avaliacao > 10:
            avaliacao = 10
        elif avaliacao < 0:
            avaliacao = 0
        
        assistiu = int(input("Quantas vezes você assistiu este filme? "))
        if assistiu < 0:
            assistiu = 0

        filme_dict = {
            "Filme": filme,
            "Ano": ano,
            "Genêro": genero,
            "Avaliação": avaliacao,
            "Vezes que você assistiu": assistiu
        }

        filmes.append(filme_dict)

    return filmes


print("Olá, bem vindo ao CineData!\n")
adicionar = input("Deseja adicionar filmes à sua lista de favoritos? (s/n): ").lower()

if adicionar == "s":
    novos_filmes = coloca_filme()

    # Lê JSON existente
    if os.path.exists("fav.json"):
        with open("fav.json", "r", encoding="utf-8") as f:
            dados_existentes = json.load(f)
    else:
        dados_existentes = []

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

else:
    print("Ok. Nada foi feito.")