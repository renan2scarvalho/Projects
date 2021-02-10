# Raspagem de Livros
---

## Objetivo :dart: :floppy_disk:

Realizar a raspagem de um web site, agregando informações em um arquivo único .csv.



## Projeto :snake: :books: :file_folder: :calendar:


O repositório contém um arquivo .py que realiza a raspagem (*web scraping*) de todas as paǵinas com livros do site [books.toscrape](http://books.toscrape.com/) utilizando a biblioteca `BeautifulSoup`, e salva os dados dos livros contidos em um arquivo .csv. Dentre as informações dos livros:

- Título :memo:
- Preço (£) :pound:
- Avaliação :star:
- Em estoque :truck:

O script está automatizado para realizar a raspagem automaticamente em um horário pré-determinado (*schedule*), realizada com a biblioteca `schedule`.


