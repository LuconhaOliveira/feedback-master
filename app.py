from flask import Flask,render_template,request,redirect
from datetime import datetime
import mysql.connector
from data.conexao import Conexao
from model.controller_mensagem import Mensagem
from model.controller_user import User



app = Flask(__name__)

@app.route("/comentario")
def pagina_comentarios():
    mensagens=Mensagem.recuperar_mensagens()
    return render_template("index.html",mensagens=mensagens)

@app.route("/post/mensagem", methods=["POST"])
def post_mensagem():
    user = request.form.get("user")
    message = request.form.get("comment")

    Mensagem.cadastrar_mensagem(user,message)
    return redirect("/comentario")
    
@app.route("/deletar/mensagem/<codigo>")
def deletar_mensagem(codigo):
    Mensagem.deletar_mensagem(codigo)
    return redirect("/comentario")

@app.route("/put/mensagem/curtida/<codigo>")
def curtir_mensagem(codigo):
    Mensagem.curtir_mensagem(codigo)
    return redirect("/comentario")

@app.route("/put/mensagem/descurtida/<codigo>")
def descurtir_mensagem(codigo):
    Mensagem.descurtir_mensagem(codigo)
    return redirect("/comentario")

@app.route("/cadastro")
def pagina_usuario():
    return render_template("user_sign.html")

@app.route("/post/cadastro", methods=["POST"])
def cadastrar_usuario():
    login = request.form.get("login")
    name = request.form.get("name")
    password = request.form.get("password")

    User.cadastrar_usuario(login,name,password)
    return redirect("/")

@app.route("/")
def pagina_login():
    return render_template("user_login.html")

@app.route("/post/login", methods=["POST"])
def login_usuario():
    login = request.form.get("login")
    password = request.form.get("password")

    User.logar_usuario(login,password)
    return redirect("/comentario")


app.run(debug=True)