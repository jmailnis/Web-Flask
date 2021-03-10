from re import M
from flask import Flask, render_template
from flask.globals import request
from flask_mysql_connector import MySQL
from mysql.connector import cursor

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DATABASE'] = 'baseconsultas'


mysql = MySQL(app)


@app.route('/')
def home():
	return render_template ("index.html")

@app.route('/agendas')
def agendas():
	return render_template ("CatalogoAgendas.html")

@app.route('/viajes')
def viajes():
	return render_template ("Viajes.html")

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
	if request.method == 'POST':
		apellido= request.form['apellido']
		nombre= request.form['nombre']
		email = request.form['email']
		telefono = request.form['telefono']
		tipo= request.form['tipo']
		cursor = mysql.connection.cursor()
		cursor.execute('INSERT INTO consultas (apellido, nombre, email, telefono, tipo ) VALUES (%s,%s,%s,%s,%s)', (apellido, nombre, email, telefono, tipo))
		mysql.connection.commit()
		cursor.close()
	
	return render_template ("Formulario.html")
@app.route('/vista')

def vista():
	cursor = mysql.connection.cursor()
	cursor.execute('SELLECT * FROM consultas ')
	clientes = cursor.fetchall()
	cursor.close()




	return render_template ("Vista.html", contacts=clientes)

if __name__ == '__main__':
	app.run(debug=True)


