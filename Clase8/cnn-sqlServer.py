'''
docker run -d \
  --name sqlserver \
  -e "ACCEPT_EULA=Y" \
  -e "SA_PASSWORD=unida123" \
  -p 1433:1433 \
  mcr.microsoft.com/mssql/server:2022-latest

'''
#pip install pymssql
'''
import pymssql

conn = pymssql.connect(
    server='localhost',
    user='sa',
    password='Passw0rd!',
    database='unidaDB'
)
cursor = conn.cursor()
cursor.execute('SELECT TOP 5 * FROM Clientes')
for row in cursor.fetchall():
    print(row)
conn.close()
'''