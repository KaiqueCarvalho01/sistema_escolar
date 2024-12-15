import sqlite3

class SistemaDeRegistro:
    def __init__(self):
        self.conexao = sqlite3.connect('usuario.db')
        self.cursor = self.conexao.cursor()

        #criando o banco de dados
        #caso não exista irá criar, caso exista irá usar o existente fazendo a conexão
        self.create_table()

    
    def create_table(self):
        #criando a tabela ALUNO
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS aluno (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL,
                                email TEXT NOT NULL,
                                senha TEXT NOT NULL,
                                telefone TEXT NOT NULL,
                                sexo TEXT NOT NULL,
                                data_nascimento TEXT NOT NULL,
                                endereco TEXT NOT NULL,
                                curso TEXT NOT NULL)''')
        
        #criando a tabela professor
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS professor (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL,
                                email TEXT NOT NULL,
                                senha TEXT NOT NULL,
                                telefone TEXT NOT NULL,
                                sexo TEXT NOT NULL,
                                data_nascimento TEXT NOT NULL,
                                endereco TEXT NOT NULL,
                                especialidade TEXT NOT NULL)''')
        
        #criando a tabela adm
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS administrador (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL,
                                email TEXT NOT NULL,
                                senha TEXT NOT NULL,
                                telefone TEXT NOT NULL)''')
        
       # self.conexao.commit()
       # self.conexao.close()
        # Salvar (commit) as mudanças e fechar a conexão 
        
    def registro_aluno(self, aluno): #função para registrar alunos
        self.cursor.execute("INSERT INTO aluno(nome, email, senha, telefone, sexo, data_nascimento, endereco, curso) VALUES (?,?,?,?,?,?,?,?)", 
                            (aluno)) #inserindo dados na tabela aluno
        self.conexao.commit() #salvando os dados no banco de dados
        

        #mostrando mensagem de sucesso
        print("Aluno registrado com sucesso!")
    
    def registro_professor(self, professor): #funcao para registrar professores
        self.cursor.execute("INSERT INTO professor(nome, email, senha, telefone, sexo, data_nascimento, endereco, especialidade) VALUES (?,?,?,?,?,?,?,?)", 
                            (professor)) #inserindo dados na tabela

        #mostrando mensagem de sucesso
        print("Professor registrado com sucesso!")

    def registro_adm(self, administrador): #função para registrar adm
        self.cursor.execute("INSERT INTO administrador(nome, email, senha, telefone) VALUES (?,?,?,?)", 
                            (administrador)) #inserindo dados
        self.conexao.commit()

        print("Administrador cadastrado com sucesso!")
        
    def visualizar_todos_alunos(self): #função para visualizar alunos
        self.cursor.execute("SELECT * FROM aluno") 
        dados = self.cursor.fetchall()  #imprimir as informações do aluno

        for i in dados:
            print(f'ID: {i[0]} | Nome: {i[1]} | E-mail: {i[2]} | Telefone: {i[3]} | Sexo: {i[4]} Data de Nascimento: {i[5]} |  Endereco: {i[6]} | Curso: {i[7]} ')

    def visualizar_todos_professores(self): #função para visualizar os professors
        self.cursor.execute("SELECT * FROM professor")
        dados = self.cursor.fetchall() #imprimir as informações do professor

        for i in dados:
            print(f'ID: {i[0]} | Nome: {i[1]} | E-mail: {i[2]} | Telefone: {i[3]} | Sexo: {4} | Data de Nascimento: {i[5]} |  Endereco: {i[6]} | Especialidade: {i[7]} ')

    def procurar_aluno(self, id): #função para procurar alunos
        self.cursor.execute("SELECT * FROM aluno WHERE id = ?", (id,)) #virgula no fundo para evitar possiveis erros
        dados = self.cursor.fetchone()

        print( print(f'ID: {dados[0]} | Nome: {dados[1]} | E-mail: {dados[2]} | Telefone: {dados[3]} | Sexo: {dados[4]}, Data de Nascimento: {dados[5]} |  Endereco: {dados[6]} | Curso: {dados[7]} '))
        

    def atualizar_aluno(self, novos_valores): #função para atualizar alunos
        query = "UPDATE aluno SET nome= ?, email = ?, senha = ?, telefone = ?, sexo = ?, data_nascimento = ?, endereco = ?, curso = ? WHERE id = ?"
        self.cursor.execute(query, novos_valores) #atualizando os dados do aluno
        self.conexao.commit() #salvando os dados no banco de dados

        #mostrando mensagem de sucesso
        print(f'Aluno: {novos_valores[8]} atualizado com sucesso!') #id
        

    def deletar_aluno(self, id): #função para deletar aluno
        self.cursor.execute("DELETE FROM aluno WHERE id = ?", (id,)) #deletando/virgula no fundo para evitar possiveis erros
        self.conexao.commit() #salvando os dados no banco de dados

        #mostrando mensagem de sucesso
        print(f'Aluno com ID: {id} deletado com sucesso!')
        
    
    def autenticar_usuario(self, email, senha):
    # Verificar na tabela aluno
        self.cursor.execute("SELECT * FROM aluno WHERE email = ? AND senha = ?", (email, senha))
        aluno = self.cursor.fetchone()
        if aluno:
            print(f'Bem-vindo de volta, {aluno[1]} (Aluno)!')  # aluno[1] é o nome
            return 'aluno'  # Retorna o tipo de usuário

        # Verificar na tabela professor
        self.cursor.execute("SELECT * FROM professor WHERE email = ? AND senha = ?", (email, senha))
        professor = self.cursor.fetchone()
        if professor:
            print(f'Bem-vindo de volta, {professor[1]} (Professor)!')  # professor[1] é o nome
            return 'professor'  # Retorna o tipo de usuário

        # Verificar na tabela administrador
        self.cursor.execute("SELECT * FROM administrador WHERE email = ? AND senha = ?", (email, senha))
        administrador = self.cursor.fetchone()
        if administrador:
            print(f'Bem-vindo de volta, {administrador[1]} (Administrador)!')  # administrador[1] é o nome
            return 'administrador'  # Retorna o tipo de usuário

        # Se não encontrar em nenhuma tabela
        print('E-mail ou senha não encontrados.')
        return None  # Retorna None se não encontrar
    
#Criando uma instância da classe de SistemaDeRegistro
sistema_de_registro = SistemaDeRegistro()


#função Cadastro
def cadastro_aluno():
        nome = input("Digite o nome do aluno: ")
        email = input("Digite o e-mail do aluno: ")
        senha = input("Digite a senha do aluno: ")
        telefone = input("Digite o telefone do aluno: ")
        sexo = input("Digite o sexo do aluno: ")
        data_nascimento = input("Digite a data de nascimento do aluno (dd/mm/aaaa): ")
        endereco = input("Digite o endereco do aluno: ")
        curso = input("Digite o curso do aluno: ")

        estudante = (nome, email, senha, telefone, sexo, data_nascimento, endereco, curso)
        return  sistema_de_registro.registro_aluno(estudante)

def cadastro_professor():
        nome = input("Digite o nome do professor: ")
        email = input("Digite o e-mail do professor: ")
        senha = input("Digite a senha do professor: ")
        telefone = input("Digite o telefone do professor: ")
        sexo = input("Digite o sexo do professor: ")
        data_nascimento = input("Digite a data de nascimento do professor (dd/mm/aaaa): ")
        endereco = input("Digite o endereco do professor: ")
        especialidade = input("Digite o curso do professor: ")

        professor_dados = (nome, email, senha, telefone, sexo, data_nascimento, endereco, especialidade)
        return sistema_de_registro.registro_professor(professor_dados)

def cadastro_adm():
    nome = input("Digite o nome do adm: ")
    email = input("Digite o e-mail do adm: ")
    senha = input("Digite a senha do adm: ")
    telefone = input("Digite o telefone do adm: ")

    adm_dados = (nome, email, senha, telefone)
    return sistema_de_registro.registro_adm(adm_dados)

def menu_autenticado(tipo_usuario):
    if tipo_usuario == 'aluno':
        print("\n-- Menu do Aluno --")
        # Adicione opções específicas para alunos
    elif tipo_usuario == 'professor':
        print("\n-- Menu do Professor --")
        # Adicione opções específicas para professores
    elif tipo_usuario == 'administrador':
        print("\n-- Menu do Administrador -- \n")
        # Adicione opções específicas para administradores
        print("1- Cadastrar Aluno")
        print("2- Cadastrar Professor")
        print("3- Cadastrar Administrador")
        print("4- Listar Alunos")
        print("5- Listar Professores")
        print("6- Listar Administradores")
        print("7- Atualizar dados")
        print("8- Sair")
        opcao = input("\n Digite a opção desejada: ")
        if opcao == "1":
            cadastro_aluno()
        elif opcao == "2":
            cadastro_professor()
        elif opcao == "3":
            cadastro_adm()
        elif opcao == "4":
            sistema_de_registro.visualizar_todos_alunos()
        elif opcao == "5":
            sistema_de_registro.visualizar_todos_professores()
        elif opcao == "6":
            sistema_de_registro.visualizar_todos_adm()
        #elif opcao == "7":
            
        elif opcao == "8":
            print("Saindo...")
            return False
        else:
            print("Opção inválida. Tente novamente.")
            return menu_autenticado(tipo_usuario)
        
    

        
#Função Autenticação
def autenticar_usuario():
    email = input("Digite o e-mail: ")
    senha = input("Digite a senha: ")
    tipo_usuario = sistema_de_registro.autenticar_usuario(email, senha)  # Chama a função de autenticação

    if tipo_usuario:  # Se a autenticação for bem-sucedida
        menu_autenticado(tipo_usuario)  # Chama o menu autenticado com o tipo de usuário


#Função Menu
def menu():
    while True:
        print("\n-- Menu --")
        print("1 - Autenticar Usuário") #
        print("0 - Sair") #
        opcao = input("Escolha uma opção: ")

        #Cadastrar Usuário
        if opcao == '1':
            autenticar_usuario()
            
        elif opcao == '0':
            print("Saindo...")
            break

        #Opção inválida
        else:
            print("Opção inválida. Tente novamente")

# Chama o menu
menu()



""" #Procurar Aluno
sistema_de_registro.procurar_aluno(1)
 """

""" #atualizar aluno
estudante = ('Joao Pereira', 'joao@gmail.com', '1234', 'M', '01/05/2005', 'Angola, Nigeira', 'Analise e Desenvolvimento de Sistemas', 1) #passar id no final
aluno = sistema_de_registro.atualizar_aluno(estudante)
 """

""" #DELETAR ALUNO
sistema_de_registro.deletar_aluno(1)
 """
