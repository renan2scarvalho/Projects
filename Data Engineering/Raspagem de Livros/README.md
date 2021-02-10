# Raspagem de Livros
---


## Objetivo :dart: :floppy_disk:

Realizar a raspagem automática de um web site, agregando informações em um arquivo único .csv, enviando um e-mail ao usuário se a raspagem for concluída com sucesso.


## Projeto :snake:   

### Raspagem :books: :file_folder:

O arquivo book_scraping.py que realiza a raspagem (*web scraping*) de todas as paǵinas com livros do site [books.toscrape](http://books.toscrape.com/) utilizando a biblioteca `BeautifulSoup`, e salva os dados dos livros contidos em um arquivo .csv. Dentre as informações dos livros:

- Título :memo:
- Preço (£) :pound:
- Avaliação :star:
- Em estoque :truck:

### Mensagem  :mailbox:

O arquivo send_email.py aplica a biblioteca `email` para enviar um e-mail automaticamente ao usuário após o fim do web scraping, caso o mesmo tenha sido realizado com sucesso.

### Jobs :calendar:

O script jobs.py utiliza as funções criadas nos scripts anteriores juntando-as em um agendamento automático em um horário pré-determinado (*schedule*) para a raspagem através da biblioteca `schedule`.

