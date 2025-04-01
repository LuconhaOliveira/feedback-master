import mysql.connector

class Conexao:

    def criar_conexao():
        conexao = mysql.connector.connect(
        host="localhost", 
        port=3306, 
        user="root", 
        password="root", 
        database="db_feedback"
        )
        return conexao