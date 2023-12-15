from flask import Flask, redirect, url_for, request, render_template
from datetime import date
from tabelas import *
from criacao import *
from consultas import *


app = Flask(__name__)

print(criar())
print(tables())
session = criar()[3]
session.commit()

@app.route("/")
def inicio():
    return render_template("index.html") 

@app.route("/index.html")
def index():
    return render_template("index.html") 

@app.route("/cadastro/cadastro.html", methods=['GET'])
def cadastro():
        username = request.args.get('username')
        email = request.args.get('email')
        password = request.args.get('password')

        print(search(f"INSERT INTO usuario(login, senha, gmail, data_criacao) VALUES ('{username}','{email}','{password}', '{date.today()}');"))
        session.commit()
        return render_template("cadastro.html")


@app.route("/lista/listagem.html", methods=['GET'])
def listagem():
    resposta = ""
    if request.args.get('login') != None:
        login = request.args.get('login')
        email = request.args.get('gmail')
        if login != "*":
            resposta = (search(f"SELECT login, gmail, data_criacao FROM usuario as u WHERE u.login='{login}' AND u.gmail='{email}';"))
        else: 
            resposta = (search(f"SELECT login, gmail, data_criacao FROM usuario;"))
            print(resposta)


    return render_template("listagem.html", resposta=resposta)

@app.route("/sobre_nos/sobre.html")
def sobre():
    return render_template("sobre.html")


@app.route("/conc/conceitos.html")
def conc():
    return render_template("conceitos.html")


if __name__ == "__main__":
    app.run(debug=True)