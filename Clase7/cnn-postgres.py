import psycopg2

# Parametros de conexion
host = "localhost"  # o la ip del servidor
port = "5432"  # puerto por defecto de postgres
database = "curso_python"
user = "postgres"
password = "2022101555ATS"

conn = None
cursor = None

try:
    # Establecer la conexion
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password,
    )

    cursor = conn.cursor()
    print("Conexion exitosa a la base de datos")

    # Crear tabla clientes si no existe
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS clientes (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            email VARCHAR(150) UNIQUE NOT NULL,
            telefono VARCHAR(20),
            fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
    )
    conn.commit()
    print("Tabla clientes verificada/creada correctamente")

    # Ejecutar una consulta de prueba
    cursor.execute("SELECT * FROM clientes LIMIT 5;")

    # Mostrar los resultados
    for row in cursor.fetchall():
        print(row)

except psycopg2.Error as error:
    print(f"Ocurrio un error al interactuar con la base de datos: {error}")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
