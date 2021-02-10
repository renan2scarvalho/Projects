# Raspagem de Livros
---

O repositório contém um arquivo .py que realiza a raspagem (*web scraping*) de todas as paǵinas do site [books.toscrape](http://books.toscrape.com/) utilizando a biblioteca `BeautifulSoup`, e salva os dados dos livros contidos em um arquivo .csv. Dentre as informações dos livros:

- Título
- Preço (£)
- Avaliação
- Em estoque

O script está automatizado para realizar a raspagem automaticamente em um horário pré-determinado (*schedule*), realizada com a biblioteca `schedule`.
