from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/miraflores')
def miraflores():
    return render_template('miraflores.html')

@app.route('/cachipay')
def cachipay():
    return render_template('cachipay.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/loteo')
def loteo():
    return render_template('loteo.html')

@app.route('/otros')
def otros():
    return render_template('otros.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
