from flask import Blueprint, request, jsonify

login = Blueprint('login', __name__) # Creación del Blueprint llamado 'login'

@login.route('/login', methods=['POST']) #Ruta del servicio: /login y función llamarServicioSet
def llamarServicioSet():
    # Procesamiento de la solicitud
    user = request.json.get('user')
    password = request.json.get('password')
    matricula = request.json.get('matricula')
    print("Headers:", request.headers)
    print(f"Usuario: {user}, Password: {password}, Matricula: {matricula}")

    codRes, menRes, accion = inicializarVariables(user, password)  # llamada a la función de verificación

    salida = { #Respuesta en formato JSON
        "codRes": codRes,
        "menRes": menRes,
        "usuario": user,
        "accion": accion        
    }
    return jsonify(salida)

def inicializarVariables(user, password): #Funcion de validación de login
    userlocal = "albertpapi"
    passlocal = "Unida123"
    codRes = "SIN_ERROR"
    menRes = "OK"
    
    try:
        print("Verificando Login")
        if password == passlocal and user == userlocal: # Validación de usuario y contraseña
            print("Login exitoso")
            accion = "Success"
        else: # caso contrario, si la validación falla
            print("Usuario o contraseña incorrecta")
            codRes = "ERROR"
            menRes = "Credenciales o usuario incorrectas"
            print("Login fallido")  
            accion = "No_Succes"
    except Exception as e: # Manejo de errores
        print("ERROR", str(e))
        codRes = ' ERROR '
        menRes = 'Msg: ' + str(e)
        accion = "Error interno"
    return codRes, menRes, accion
    
