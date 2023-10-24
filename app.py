from flask import Flask, render_template, request, redirect, url_for

from flask_mail import Mail, Message


app = Flask(__name__)
# la info se saco de mailtrap
app.config['MAIL_SERVER'] = 'sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '5d8e0af960a014'
app.config['MAIL_PASSWORD'] = '13ca3f58e88c5c'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mail', methods=['GET', 'POST'])
def send_mail():

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        msg = Message(
            'Hola Edward, tienes un nuevo contacto desde la web:',
            body=f'Nombre: {name} \nCorreo: <{email}> \n\nMensaje: \n\n{message}',
            sender=email,
            recipients=['edwardmaz13@gmail.com']
        )

        # pantalla de correo exitoso

        mail.send(msg)
        return render_template('send_mail.html')

    return redirect(url_for('index'))
