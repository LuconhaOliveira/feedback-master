import datetime
from data.conexao import Conexao


class Mensagem:

    def cadastrar_mensagem(user,message):
        data_hora = datetime.datetime.today()

        conexao = Conexao.criar_conexao()
        cursor = conexao.cursor(dictionary=True)

        sql = "INSERT INTO tb_comentarios(nome,data_hora,comentario,curtidas) VALUES(%s,%s,%s,0);"
        valores=(user,data_hora,message)

        cursor.execute(sql,valores)
        conexao.commit()
        cursor.close()
        conexao.close()
    
    def recuperar_mensagens():
        conexao = Conexao.criar_conexao()
        cursor=conexao.cursor(dictionary=True)
        sql="select nome,comentario,data_hora,curtidas,cod_comentario from tb_comentarios;"
        cursor.execute(sql)
        resultado=cursor.fetchall()

        cursor.close()
        conexao.close()
        
        return resultado
    
    def deletar_mensagem(cod_mensagem):
        conexao = Conexao.criar_conexao()
        
        cursor=conexao.cursor(dictionary=True)
        sql="DELETE FROM tb_comentarios WHERE cod_comentario = %s;"
        valores=(cod_mensagem,)
        cursor.execute(sql,valores)
        conexao.commit()
        cursor.close()
        conexao.close()
        
    def curtir_mensagem(cod_mensagem):
        conexao = Conexao.criar_conexao()
        
        cursor=conexao.cursor(dictionary=True)
        sql="UPDATE tb_comentarios SET curtidas = curtidas+1 WHERE cod_comentario=%s;"
        valores=(cod_mensagem,)
        cursor.execute(sql,valores)
        conexao.commit()
        cursor.close()
        conexao.close()

    def descurtir_mensagem(cod_mensagem):
        conexao = Conexao.criar_conexao()
        
        cursor=conexao.cursor(dictionary=True)
        sql="UPDATE tb_comentarios SET curtidas = curtidas-1 WHERE cod_comentario=%s;"
        valores=(cod_mensagem,)
        cursor.execute(sql,valores)
        conexao.commit()
        cursor.close()
        conexao.close()
    