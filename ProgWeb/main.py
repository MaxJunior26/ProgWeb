
from flask import Flask, render_template
from lib import DadosAbertos

app = Flask(__name__)

@app.route("/")
def deputados():
   obj = DadosAbertos()
   list_dep = obj.deputados()

   return render_template('lista.html', listas=list_dep)

@app.route("/eventos/<id>")
def deputado(id):
   obj    = DadosAbertos()
   info   = obj.deputado_id(id)
   eventos = obj.deputado_eventos(id)
   orgao   = obj.deputado_orgaos(id)
   

   return render_template('showEvents.html', event=eventos, org = orgao)   





if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True, port=8080)