# Sistema de Recomendação de Cursos
---

O projeto consistiu na utilização de uma base de dados de usuários de diferentes tipos de cursos, os quais abordam diferentes linguagens de programação, para criar um simples sistema de recomendação baseando-se nas linguagens mais utilizadas pelos usuários, bem como nos cursos ainda não realizados e média de avaliação por curso aplicando um threshold arbitrário de avaliação (regras de negócio). O banco de dados pode ser encontrado em [[1]](https://raw.githubusercontent.com/qodatecnologia/postgresql-db-reviews/main/db.sql).

A base de dados foi inserida no SGBD PostgreSQL, e posteriormente chamada no notebook através da conexão uri, utilizando as bibliotecas `sqlachemy`, `psycopg2`, e `pandas`, com queries SQL. Após a realização da recomendação, ao final, o df é enviado novamente ao PostgreSQL em uma nova base de dados (DW).
