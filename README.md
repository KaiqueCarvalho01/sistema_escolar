# Sistema Escolar em Python

Este projeto é um **sistema escolar** desenvolvido em Python, utilizando o banco de dados SQLite3, com o objetivo de gerenciar o cadastro e a atualização de informações sobre alunos, professores e administradores. O sistema permite a interação com dados como notas dos alunos e acessos restritos de acordo com o perfil de cada usuário.

## Tecnologias utilizadas

- **Python 3.x**: Linguagem de programação utilizada para o desenvolvimento do sistema.
- **SQLite3**: Banco de dados leve utilizado para armazenar as informações no arquivo `usuario.db`.

## Funcionalidades

### Para Administradores:
- **Cadastro de alunos**: Adicionar novos alunos ao sistema.
- **Cadastro de professores**: Adicionar novos professores ao sistema.
- **Cadastro de administradores**: Adicionar novos administradores ao sistema.
- **Edição de dados**: Atualizar informações de alunos, professores e administradores.
- **Exclusão de dados**: Remover alunos, professores e administradores do sistema.

### Para Professores:
- **Atribuição de notas**: Professores podem atribuir notas aos alunos.
  
### Para Alunos:
- **Consulta de notas**: Alunos podem visualizar suas próprias notas no sistema.

## Arquivo de banco de dados

O sistema utiliza um banco de dados SQLite3 chamado `usuario.db`, onde são armazenadas todas as informações dos usuários (alunos, professores e administradores), como nome, login, senha e notas atribuídas.

## Estrutura do banco de dados

O banco de dados possui as seguintes tabelas:

- **usuarios**: Armazena informações dos usuários (alunos, professores e administradores), como nome, login, senha e tipo de usuário.
- **notas**: Armazena as notas atribuídas aos alunos pelos professores.

## Como rodar o projeto

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/Kaiqueh1/sistema_escolar.git
2. **Certifique que o Python 3 está instalado.**
3. **Rodando o sistema**:
   Para rodar o sistema, execute o script principal do projeto main.py ou use o seguinte comando no terminal:
    ```bash
   python main.py
4. **Acessando o sistema**:
   Ao rodar o programa, será apresentado um menu com as opções disponíveis de acordo com o tipo de usuário (Administrador, Professor ou Aluno).
   Para acessar as funções do administrador, use admin como login no e-mail e senha

## Contribuições
Sinta-se à vontade para contribuir com o projeto! 

