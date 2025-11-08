from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'clave_super_secreta'  # Necesario para usar flash()

# --- RUTAS PRINCIPALES ---

@app.route('/')##
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return "<h1>Acerca del Proyecto Flask</h1><p>Página en construcción.</p>"

@app.route('/contact', methods=['POST'])
def contact():
    nombre = request.form.get('name')
    correo = request.form.get('email')
    mensaje = request.form.get('message')

    # Aquí podrías guardar los datos en una base de datos o enviar un correo
    print(f"📩 Mensaje recibido: {nombre} | {correo} | {mensaje}")

    flash("Tu mensaje ha sido enviado correctamente. ¡Gracias por contactarnos!", "success")
    return redirect(url_for('home'))

# --- PUNTO DE ENTRADA ---
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
