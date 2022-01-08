import mysql.connector

#Efetuar a conexão com o DB
banco = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='teste'
)

#Criar o banco de dados
cursor = banco.cursor()
cursor.execute('CREATE DATABASE teste')

#Criar a tabale do banco de dados
cursor = banco.cursor()
cursor.execute('CREATE TABLE pessoas (nome VARCHAR(255), idade INT (3), email VARCHAR (255))')

#Inserir dados na tabela
comando_SQL = 'INSERT INTO pessoas (nome,idade,email) VALUES (%s,%s,%s)'
dados = ('Matheus, 20, matheus@gmail.com')

#Enviar os dados
cursor = banco.cursor()
cursor.execute(comando_SQL, dados)
banco.commit()
