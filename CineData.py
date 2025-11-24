import json
filmes_fav = {}
def coloca_filme():
    q = int(input("Quantos filmes deseja adicionar aos favoritos?"))
    for i in range(q):
        filme = str(input("Nome do filme:"))
        ano = int(input("Ano de lançamento:"))
        genero = str(input("Genero:"))
        filmes_fav["filme"] = filme
        filmes_fav["ano"] = ano
        filmes_fav["genero"] = genero
        return filmes_fav

print("Olá, bem vindo ao CineData!/n")
adicionar = ("Deseja adicionar filmes a sua lista de favoritos? (s/n)").lower()

if adicionar == "s":
    coloca_filme()