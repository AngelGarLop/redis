import redis
conexionRedis = redis.ConnectionPool(host='localhost', port=6379, db=0,decode_responses=True)
baseDatosRedis = redis.Redis(connection_pool=conexionRedis)

print("1 - Crear registros clave-valor")

baseDatosRedis.set("semaforo_1","calle a")
baseDatosRedis.set("semaforo_2","calle b")

print("2 - Obtener y mostrar el número de claves registradas")

claves = baseDatosRedis.dbsize()
print(claves)

print("3 - Obtener y mostrar un registro en base a una clave")

print(baseDatosRedis.get("semaforo_1"))

print("4 - Actualizar el valor de una clave y mostrar el nuevo valor")

baseDatosRedis.set("semaforo_1","calle c")
print(baseDatosRedis.get("semaforo_1"))

print("5 - Eliminar una clave-valor y mostrar la clave y el valor eliminado")

valor=baseDatosRedis.get("semaforo_1")
baseDatosRedis.delete("semaforo_1")

print("Se ha eliminado la clave semaforo_1 y el valor "+str(valor))

print("6 - Obtener y mostrar todas las claves guardadas (0.5 puntos)")

claves = baseDatosRedis.keys()
print(claves)

print("7 - Obtener y mostrar todos los valores guardados")

valores = baseDatosRedis.mget(baseDatosRedis.keys())
print(valores)

print("8 - Obtener y mostrar varios registros con una clave con un patrón en común usando *")
claves_patron = baseDatosRedis.keys('semaforo_*')
valores_patron = baseDatosRedis.mget(claves_patron)
print(valores_patron)

print("9 - Obtener y mostrar varios registros con una clave con un patrón en común usando []")
claves_patron = baseDatosRedis.keys('semaforo_[12]')
valores_patron = baseDatosRedis.mget(claves_patron)
print(valores_patron)

print("10 - Obtener y mostrar varios registros con una clave con un patrón en común usando ?")
claves_patron = baseDatosRedis.keys('semaforo_?')
valores_patron = baseDatosRedis.mget(claves_patron)
print(valores_patron)

print("11 - Obtener y mostrar varios registros y filtrarlos por un valor en concreto.")
valores = baseDatosRedis.mget(baseDatosRedis.keys())
valores_filtrados = [ v for v in valores if v == 'calle a']
print(valores_filtrados)

print("12 - Actualizar una serie de registros en base a un filtro (por ejemplo aumentar su valor en 1)")
for clave in baseDatosRedis.keys('semaforo_*'):
    valor = baseDatosRedis.get(clave)
    if valor.isdigit():
        baseDatosRedis.set(clave, int(valor) + 1)
    else:
        baseDatosRedis.set(clave, valor + '1')
print(baseDatosRedis.mget(baseDatosRedis.keys('semaforo_*')))

print("13 - Eliminar una serie de registros en base a un filtro")
for clave in baseDatosRedis.keys('semaforo_*'):
    baseDatosRedis.delete(clave)
print(baseDatosRedis.keys('semaforo_*'))

print("14 - Crear una estructura en JSON de array de los datos que vayais a almacenar")
import json
datos = [
    {"id": 1, "nombre": "semaforo_1", "ubicacion": "calle a"},
    {"id": 2, "nombre": "semaforo_2", "ubicacion": "calle b"}
]
baseDatosRedis.set('datos_json', json.dumps(datos))
print(baseDatosRedis.get('datos_json'))

print("15 - Realizar un filtro por cada atributo de la estructura JSON anterior")
datos_json = json.loads(baseDatosRedis.get('datos_json'))
filtro_id = [d for d in datos_json if d['id'] == 1]
filtro_nombre = [d for d in datos_json if d['nombre'] == 'semaforo_1']
filtro_ubicacion = [d for d in datos_json if d['ubicacion'] == 'calle a']
print(filtro_id, filtro_nombre, filtro_ubicacion)

print("16 - Crear una lista en Redis")
baseDatosRedis.rpush('lista_semaforos', 'semaforo_1', 'semaforo_2')
print(baseDatosRedis.lrange('lista_semaforos', 0, -1))

print("17 - Obtener elementos de una lista con un filtro en concreto")
lista_semaforos = baseDatosRedis.lrange('lista_semaforos', 0, -1)
filtro_lista = [item for item in lista_semaforos if '1' in item]
print(filtro_lista)

print("18 - Crear y obtener datos usando Set y Hashes en Redis")
# Set
baseDatosRedis.sadd('set_semaforos', 'semaforo_1', 'semaforo_2')
print(baseDatosRedis.smembers('set_semaforos'))

# Hashes
baseDatosRedis.hset('hash_semaforo_1', mapping={'ubicacion': 'calle a', 'estado': 'verde'})
print(baseDatosRedis.hgetall('hash_semaforo_1'))



