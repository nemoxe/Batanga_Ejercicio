#REQUERIMIENTOS
#Instalar los modulos dnspython y requests, usando pip install

#Se importan los modulos

import dns.resolver
import requests

#Se declaran 3 variables: domain, domain2 y mail, en las cuales se guarda la direccion del sitio del cual obtendremos los registros A,
#la direccion del sitio al cual realizaremos los pedidos GET
#y la direccion de mail que se pasara como argumento, respectivamente.

domain = 'imujer.com'
domain2 = 'http://199.34.125.35/test'
mail = 'nemoxe@gmail.com'


#Se utiliza la funcion query del modulo dns.resolver para obtener los registros A de domain y se guardan en la variable records

records = dns.resolver.query(domain,'A')



#En este loop, para cada valor de la variable records se imprime en pantalla una frase ejemplificando el GET,
#se realiza la request utilizando la funcion get del modulo requests con los argumentos requeridos por el ejercicio
#y se muestra el codigo http devuelto por la request GET

for record in records:
	
	print "Realizando request GET con los argumentos: " + 'email= ' + mail  + ' record= ' + str(record)
	r = requests.get(domain2 + '?email=' + mail + '&record=' + str(record))
	print "La request GET devolvio el siguiente status: " + "http code " + str(r.status_code) + "\n"
