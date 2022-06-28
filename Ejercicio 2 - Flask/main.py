from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
# Página de inicio
@app.route('/')
def home():
  return render_template('home.html')
  

# Explica de que trata la página
@app.route('/ayuda')
def acercaDe():
  return render_template('ayuda.html')

#Muestra el Top 10 per capita de todos los paises 
@app.route('/listado')
def topPerCapita():
 
  conn = sqlite3.connect('co_emissions.db')
  q = f"""SELECT Country, Value FROM emissions WHERE
  Series = 'pcap' ORDER BY Value desc"""
  resu = conn.execute(q)
  
  top10pcap = []
  for i in resu:
    top10pcap.append(i)
      
  conn.close()
 
  return render_template("perCapita.html",
                         Top10 = top10pcap)


#Muestra el top 10 Total de todos los paises
@app.route('/listado/top')
def topTotal():
  
  conn = sqlite3.connect('co_emissions.db')
  q = f"""SELECT Country, Value FROM emissions WHERE
  Series = 'total' ORDER BY Value desc"""
  resu = conn.execute(q)
  
  toptotal = []
  for i in resu:
    toptotal.append(i)
      
  conn.close()
  return render_template("total.html",  Top10 = toptotal)


#Según país ingresado muestra los 10 primeros valores de Total y per capita
@app.route('/listado/<pais>')
def totalYPerCapitaPorPais(pais):
  
  conn = sqlite3.connect("co_emissions.db")
  q = f"""SELECT Country, Series, Value FROM emissions WHERE Country =
  '{pais}' ORDER BY Value desc"""
  resu = conn.execute(q)
  
  topPais = []
  for i in resu:
    topPais.append(i)
    
  conn.close()
  return render_template("topPais.html", TopPais = topPais)
  

  
app.run(host='0.0.0.0', port=81)