import redis
conexionRedis = redis.ConnectionPool(host='localhost', port=6379, db=0,decode_responses=True)
baseDatosRedis = redis.Redis(connection_pool=conexionRedis)

#1 - Crear registros clave-valor(0.5 puntos)

#baseDatosRedis.set("semaforo_1","calle a")
#baseDatosRedis.set("semaforo_2","calle b")

#2 - Obtener y mostrar el número de claves registradas (0.5 puntos)

#claves = baseDatosRedis.dbsize()
#print(claves)

#3 - Obtener y mostrar un registro en base a una clave (0.5 puntos)

#print(baseDatosRedis.get("semaforo_1"))

#4 - Actualizar el valor de una clave y mostrar el nuevo valor(0.5 puntos)

#baseDatosRedis.set("semaforo_1","calle c")
#print(baseDatosRedis.get("semaforo_1"))

#5 - Eliminar una clave-valor y mostrar la clave y el valor eliminado(0.5 puntos)

#valor=baseDatosRedis.get("semaforo_1")
#baseDatosRedis.delete("semaforo_1")
#print("Se ha eliminado la clave semaforo_1 y el valor "+str(valor))

#6 - Obtener y mostrar todas las claves guardadas (0.5 puntos)

#claves = baseDatosRedis.keys()
#print(claves)

#7 - Obtener y mostrar todos los valores guardados(0.5 puntos)

claves = baseDatosRedis.keys()

for clave in claves:
	valor=baseDatosRedis.get(clave)
 	print("Valor: "+ str(valor))
