
'''
docker run -d \
  --name mysql-db \
  -e MYSQL_ROOT_PASSWORD=unida123 \
  -e MYSQL_DATABASE=jaguarete \
  -e MYSQL_USER=unida \
  -e MYSQL_PASSWORD=unida123 \
  -p 3306:3306 \
  mysql:latest

'''
#pip install pymysql

'''
import pymysql

# Parámetros de conexión
host = "localhost"
port = 3306
user = "unida"
password = "unida123"
database = "jaguarete"

try:
    # Crear conexión
    conn = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
    print("✅ Conectado a MySQL en Docker")

    # Crear cursor
    cursor = conn.cursor()

    # Crear tabla de ejemplo
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100),
        ciudad VARCHAR(100)
    );
    """)

    # Insertar datos
    cursor.execute("INSERT INTO clientes (nombre, ciudad) VALUES (%s, %s)", ("Juan", "Asunción"))
    conn.commit()

    # Leer datos
    cursor.execute("SELECT * FROM clientes;")
    for row in cursor.fetchall():
        print(row)

except Exception as e:
    print("❌ Error al conectar:", e)

finally:
    if 'conn' in locals():
        conn.close()
'''