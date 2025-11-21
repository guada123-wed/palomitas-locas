app.py
from flask import *
import mysql.connector
 #Conexión a la base de datos
conexion = mysql.connector.connect(
host="localhost",
user="root",
password="root",
database="peliculas_reviews"
)
cursor = conexion.cursor()

app = Flask(__name__)

@app.route('/')
def index():
    query = "SELECT * FROM Reviews"
    cursor.execute(query)
    reviews = cursor.fetchall()
    return render_template('index.html', index = index)

@app.route('/eliminarreview')
def eliminarreview():
    query = "SELECT * FROM Reviews"
    cursor.execute(query)
    eliminarreview = cursor.fetchall()
    return render_template('eliminarreview.html', eliminarreview = eliminarreview)

@app.route('/entrar')
def entrar():
    query = "SELECT * FROM Reviews"
    cursor.execute(query)
    entrar = cursor.fetchall()
    return render_template('entrar.html', entrar = entrar)


@app.route('/entrarensistema')
def entrarensistema():
    query = "SELECT * FROM Reviews"
    cursor.execute(query)
    entrarensistema = cursor.fetchall()
    return render_template('entrarensistema.html', entrarensistema =entrarensistema)

@app.route('/hacerreview')
def hacerreview():
    query = "SELECT * FROM Reviews"
    cursor.execute(query)
    hacerreview= cursor.fetchall()
    return render_template('hacerreview.html', hacerreview = hacerreview)

@app.route('/verpeliculas')
def verpeliculas():
    query = "SELECT * FROM Reviews"
    cursor.execute(query)
    verpeliculas = cursor.fetchall()
    return render_template('verpeliculas.html', verpeliculas = verpeliculas)

@app.route('/verpersonas')
def verpersonas():
    query = "SELECT * FROM Reviews"
    cursor.execute(query)
    verpersonas = cursor.fetchall()
    return render_template('verpersonas.html', verpersonas = verpersonas)



@app.route('/verpeliculas', methods=['POST'])
def reviews():
    #Obtengo el titulo que puso en el formulario
    titulo_pelicula = request.form.get('titulo')
    #Hago la query en la base de datos para buscar los datos de las reseñas de esa pelicula
    query = "SELECT * FROM Peliculas   WHERE peliculas.titulo= %s titulo_pelicula" 
    cursor.execute(query)
    lista_reviews = cursor.fetchall()
    return render_template('reviews.html',lista_reviews=lista_reviews)


if __name__ == '__main__':
  app.run(debug=True)