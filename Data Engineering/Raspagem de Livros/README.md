# Raspagem de Livros
---


## Objetivo :dart: :floppy_disk:

Realizar a raspagem automática de um web site, agregando informações em um arquivo único .csv, enviando um e-mail ao usuário se a raspagem for concluída com sucesso.


## Projeto :snake:   

### Raspagem :books: :file_folder:

O repositório contém um arquivo .py que realiza a raspagem (*web scraping*) de todas as paǵinas com livros do site [books.toscrape](http://books.toscrape.com/) utilizando a biblioteca `BeautifulSoup`, e salva os dados dos livros contidos em um arquivo .csv. Dentre as informações dos livros:

- Título :memo:
- Preço (£) :pound:
- Avaliação :star:
- Em estoque :truck:

### Agendamento :calendar: :mailbox:

O script aplica as bibliotecas `schedule` e `email`para automatização, realizando a raspagem em um horário pré-determinado (*schedule*), e enviando um e-mail ao usuário ao final da raspagem.


