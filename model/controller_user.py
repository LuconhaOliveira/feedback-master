from hashlib import sha256
from data.conexao import Conexao

class User:
    name_logged = ""
    login_logged = ""

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
        sql="SELECT login,senha,nome FROM tb_usuarios WHERE login=%s AND binary senha=%s"
        valores=(login,password)
        cursor.execute(sql,valores)
        resultado=cursor.fetchone()
        if resultado:
            name_logged=resultado["nome"]
            login_logged=resultado["login"]
            return True
        else:
            return False

