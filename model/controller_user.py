from hashlib import sha256

from flask import session
from data.conexao import Conexao

class User:

    def cadastrar(login,name,password):
        password = sha256(password.encode()).hexdigest()    
        conexao = Conexao.criar_conexao()
        cursor = conexao.cursor(dictionary=True)

        sql = "INSERT INTO tb_usuarios(login,nome,senha) VALUES(%s,%s,%s);"
        valores=(login,name,password)

        cursor.execute(sql,valores)
        conexao.commit()
        cursor.close()
        conexao.close()

    def logar(login,password):
        password = sha256(password.encode()).hexdigest()
        conexao = Conexao.criar_conexao()
        cursor=conexao.cursor(dictionary=True)
        sql="SELECT login,nome FROM tb_usuarios WHERE login=%s AND binary senha=%s"
        valores=(login,password)
        cursor.execute(sql,valores)
        resultado=cursor.fetchone()
        if resultado:
            session["user_logged"]=resultado["login"]
            session["name_logged"]=resultado["nome"]
            return True
        else:
            return False

    def deslogar():
        session.clear()
