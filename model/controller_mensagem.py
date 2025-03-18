import datetime
from data.conexao import Conexao


class Mensagem:

    def cadastrar_mensagem(user,message):
        data_hora = datetime.now()

        con = Conexao.criar_conexao()
        cursor = con.cursor()

        sql = "INSERT INTO tb_Comentarios(nome,datahora,comentario) VALUES(%a,%b,%c);"
        valores=(user,data_hora,message)

        cursor.execute(sql,valores)
        cursor.close
        con.close
    
    def recuperar_mensagens():
        conexao = Conexao.criar_conexao()
        cursor=conexao.cursor(dictionary=True)
        sql="select nome,comentario,datahora from tb_comentarios;"
        cursor.execute(sql)
        resultado=cursor.fetchall()

        cursor.close()
        conexao.close()
        
        return resultado
    
    def deletar_mensagem(cod_mensagem){
        conexao = Conexao.criar_conexao()
        
        cursor=conexao.cursor(dictionary=True)
        sql="DELETE FROM tb_comentarios WHERE codcomentario = %s;"
        cursor.execute(sql,cod_mensagem)
        conexao.commit()
        cursor.close()
        conexao.close()
    }