from flask import Flask, request, redirect, url_for, render_template_string
import mysql.connector

# Configuración de la aplicación Flask
app = Flask(__name__)

# Configuración de la conexión a MariaDB
db_config = {
    'host': 'localhost',      # Cambia si MariaDB está en otro servidor
    'user': 'tu_usuario',     # Reemplaza con tu usuario de MariaDB
    'password': 'tu_contraseña', # Reemplaza con tu contraseña de MariaDB
    'database': 'usuarios_db' # Base de datos que creaste
}

# Ruta para mostrar el formulario
@app.route('/')
def formulario():
    return render_template_string("""
    <form action="/formulario" method="post">
        <input name="correo" placeholder="Correo electrónico" type="text" required />
        <input name="contraseña" placeholder="Contraseña" type="password" required />
        <button type="submit">Enviar</button>
    </form>
    """)

# Ruta para procesar el formulario y guardar los datos
@app.route('/formulario', methods=['POST'])
def guardar_formulario():
    correo = request.form.get('correo')  # Obtener el valor del campo "correo"
    contraseña = request.form.get('contraseña')  # Obtener el valor del campo "contraseña"
    
    # Conectar a la base de datos y guardar los datos
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO usuarios (correo, contraseña) VALUES (%s, %s)
    ''', (correo, contraseña))
    conn.commit()  # Confirmar la inserción en la base de datos
    cursor.close()
    conn.close()
    
    return "Datos guardados exitosamente"

if __name__ == '__main__':
    app.run(debug=True)
