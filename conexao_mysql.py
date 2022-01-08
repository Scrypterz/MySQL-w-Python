import mysql.connector

banco = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='teste'
)


cursor = banco.cursor()
cursor.execute('CREATE DATABASE teste')



cursor = banco.cursor()
cursor.execute('CREATE TABLE pessoas (nome VARCHAR(255), idade INT (3), email VARCHAR (255))')

comando_SQL = 'INSERT INTO pessoas (nome,idade,email) VALUES (%s,%s,%s)'
dados = ('Matheus, 20, matheus@gmail.com')

cursor = banco.cursor()
cursor.execute(comando_SQL, dados)
banco.commit()