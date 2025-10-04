from flask import Flask
from login import login

app = Flask(__name__)

#servicio de rest
app.register_blueprint(login)

@app.route('/', methods=['GET', 'POST'])
def home():
    return "Hola UNIDA, expertos en Python"

if __name__ == '__main__':
    
    app.run(host = '0.0.0.0', debug = True, port = 5001)
    #app.run(debug = True)
    
    