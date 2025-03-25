from data.conexao import Conexao

class User:
    name_logged = ""
    login_logged = ""

    def cadastrar_usuario(login,name,password):
        conexao = Conexao.criar_conexao()
        cursor = conexao.cursor(dictionary=True)

        sql = "INSERT INTO tb_usuarios(login,nome,senha) VALUES(%s,%s,%s);"
        valores=(login,name,password)

        cursor.execute(sql,valores)
        conexao.commit()
        cursor.close()
        conexao.close()

    def logar_usuario(login,password):
        conexao = Conexao.criar_conexao()
        cursor=conexao.cursor(dictionary=True)
        sql="SELECT login,senha,nome FROM tb_usuarios WHERE login=%s AND senha=%s"
        valores=(login,password)
        cursor.execute(sql,valores)
        resultado=cursor.fetchone()
        if resultado:
            name_logged=resultado["nome"]
            login_logged=resultado["login"]

