<!-- Relatório -->

*Alunos:*
Isabela Nóbrega, Jefte Vitor, Anny Luyrara, Jayane Stefanny.

<!-- Resumo do Programa CINEdata -->

O CINEdata é um sistema desenvolvido com o objetivo de gerenciar informações relacionadas aos filmes favoritos do usuário de maneira simples, organizada e eficiente. O programa permite adicionar, armazenar, exibir, avaliar e pesquisar filmes utilizando estruturas de dados do Python e a biblioteca json, que possibilita o salvamento das informações em arquivo de forma estruturada e permanente.
Dessa forma, o CINEdata oferece ao usuário uma experiência prática e intuitiva para registrar seus filmes preferidos, consultar listas já existentes, avaliar produções e registrar quantas vezes assistiu cada filme. O projeto foi elaborado para demonstrar a aplicação de manipulação de arquivos, listas, dicionários e interação com o usuário, reunindo diversos conceitos fundamentais de programação.

<!-- Introdução -->

Neste projeto utilizamos a biblioteca json do Python, cuja finalidade é facilitar a manipulação, leitura e gravação de dados estruturados em arquivos. O uso dessa biblioteca permite armazenar informações de forma organizada, simples e eficiente, garantindo maior praticidade no tratamento e na persistência dos dados durante o funcionamento do sistema.

<!-- Funcionalidades Implementadas -->

*Adicionar Filme aos Favoritos*

O sistema oferece ao usuário a opção de adicionar um filme à sua lista de favoritos.
Se o usuário desejar adicionar:
O filme informado é incluído em uma lista e armazenado em um dicionário.

<!-- Além do nome do filme, o usuário também pode: -->

-Avaliar o filme (por exemplo, de 1 a 5 estrelas);-

-Registrar quantas vezes assistiu ao filme.-

*Se o usuário não desejar adicionar:*

Nenhum dado é armazenado.

<!-- Armazenamento dos Dados no Arquivo -->

Após qualquer atualização da lista de filmes favoritos, o dicionário é convertido para o formato JSON e gravado em um arquivo.
 Isso garante que:
os dados sejam mantidos mesmo após o encerramento do programa;

*Exibição da Lista de Filmes*

O sistema permite que o usuário visualize todos os filmes previamente salvos no arquivo JSON.
Se o usuário optar por exibir:
O programa mostra:

-o nome dos filmes favoritos e ano de lançamento;-

-a avaliação atribuída;-

-o número de vezes assistido.-

*Se o usuário optar por não exibir:*

Nenhuma lista é apresentada durante a execução.

<!-- Busca por um Filme -->
A aplicação disponibiliza uma função específica para pesquisar filmes cadastrados.
Se o usuário desejar buscar:
O sistema verifica se o filme informado está presente na lista;

Caso esteja, são exibidas as informações completas sobre ele:

-nome do filme e ano;-

-avaliação do usuário;-

-quantidade de vezes assistido.-

Quando o usuário procurasse por um filme favorito apareceria  o nome do filme, o ano de lançamento, a avaliação que o usuário deu para ele e a posição no qual o filme se encontra nos ranking de mais bem avaliado e de mais assistido.

*Se o usuário não desejar buscar:*
Nenhuma ação de pesquisa é realizada.

<!-- Ranking -->

Ao final do código o usuário poderá olhar ao seu top 10 filmes mais assistidos e o top 10 dos filmes mais avaliados, segundo o usuário.


<!-- Conclusão -->

O uso da biblioteca json permitiu estruturar as informações de maneira eficiente, garantindo simplicidade tanto na leitura quanto na escrita dos dados. As funcionalidades de adicionar, exibir, avaliar e buscar filmes tornam o sistema CINEdata uma ferramenta prática, funcional e acessível ao usuário.
O projeto evidencia a importância do armazenamento estruturado, da interação com o usuário e da organização dos dados, ao mesmo tempo em que reforça conceitos importantes da programação em Python.
