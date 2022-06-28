from flask import Flask
import random
from datetime import date

app = Flask(__name__)

@app.route('/')
def index():
  return "Home"

@app.route('/dado')
def numAzar():
    nums = ["1", "2", "3", "4", "5", "6"]
    str = random.choice(nums)
    return str

@app.route('/fecha')
def fechas():
    inicio = date(1970, 1, 1)
    final =  date(2100, 12, 31)

    random_date = inicio + (final - inicio) * random.random()

    return str(random_date)

@app.route('/color')
def colors():
    colores = ["Negro", "Azul", "Violeta", "Rojo", "Verde", "Amarillo"]
    str = random.choice(colores)
    return str

@app.route('/dado/<n>')
def dado(n):  
  n = int(n)
  if n >= 0 and n < 11:
      lista = []
      for i in range(n):
        num = random.randint(1,6)   
        lista.append(num)
      return str(lista)
  else:
      print("Debe ser un un numero entre 1 y 10.")

@app.route('/fecha/<y>')
def fechaAño(y):
  y = int(y)
  inicio = date(y, 1, 1)
  final =  date(y, 12, 31)

  random_date = inicio + (final - inicio) * random.random()
  return str(random_date)
             

@app.route('/fecha/<y>/<m>')
def Año_Mes(y, m):
  y = int(y)
  m = int(m)
  if m >= 1 and m <= 12:
    inicio = date(y, m, 1)
    final =  date(y, m, 31)
  else:
    print("El número de mes no es valido")
    
  random_date = inicio + (final - inicio) * random.random()
  return str(random_date)
app.run(host='0.0.0.0', port=81)
