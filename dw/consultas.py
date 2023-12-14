from criacao import *
import sqlalchemy as sa



def search(code):
    engine = criar()[0]
    if not "SELECT" in code:
        try:
            sql = sa.text(code)
            engine.execute(sql)
            return f"Codigo: {code} executado com sucesso"

        except Exception as error:
            return error 
    else:
        try:
            sql = sa.text(code)
            resultado = engine.execute(sql)
            resultado = resultado.mappings().all() 

            string = ""
            for i in resultado:
                string += f"Usuario: {i['login']}       email:{i['gmail']}      conta criada em:{str(i['data_criacao'])}  \n"
            return string

        except Exception as error:
            return error