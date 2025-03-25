from flask import Flask,render_template,request,redirect
from datetime import datetime
import mysql.connector
from data.conexao import Conexao
from model.controller_mensagem import Mensagem



app = Flask(__name__)

@app.route("/")
def paginaprincipal():
    mensagens=Mensagem.recuperar_mensagens()
    return render_template("index.html",mensagens=mensagens)

@app.route("/post/mensagem", methods=["POST"])
def post_mensagem():
    user = request.form.get("user")
    message = request.form.get("comment")

    Mensagem.cadastrar_mensagem(user, message)
    return redirect("/")
    
@app.route("/deletar/mensagem/<codigo>")
def deletar_mensagem(codigo):
    Mensagem.deletar_mensagem(codigo)
    return redirect("/")

@app.route("/put/mensagem/curtida/<codigo>")
def curtir_mensagem(codigo):
    Mensagem.curtir_mensagem(codigo)
    return redirect("/")

@app.route("/put/mensagem/descurtida/<codigo>")
def descurtir_mensagem(codigo):
    Mensagem.descurtir_mensagem(codigo)
    return redirect("/")


app.run(debug=True)