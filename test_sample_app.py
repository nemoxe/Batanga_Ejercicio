#REQUERIMIENTOS
#Instalar el modulo requests, usando pip install

#Se importan los modulos

import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Sitio de sample-app
sitio = "http://127.0.0.1:3000"

#Definicion de funcion para enviar mails usando gmail
def send_mail():
        msg = MIMEMultipart()
        msg['From'] = 'ejercicio.batanga@gmail.com'
        msg['To'] = 'guzman.braso+sample-alert@batangamedia.com'
        msg['Subject'] = 'Sample-APP CAIDA'
        message = 'ALERTA SAMPLE-APP CAIDA!!\nREVISAR ASAP!!'
        msg.attach(MIMEText(message))
        mailserver = smtplib.SMTP('smtp.gmail.com',587)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.ehlo()
        mailserver.login('ejercicio.batanga@gmail.com', 'zarasa10')
        mailserver.sendmail('ejercicio.batanga@gmail.com','guzman.braso+sample-alert@batangamedia.com',msg.as_string())
        mailserver.quit()

#En este bloque se trata de hacer una request pidiendo los headers de sitio,
#si el servidor no devuelve ninguno, se imprime un mensaje en pantalla y se manda mail.
#Si el servidor devuelve algun header, se toma el codigo status http y si no es igual a 200, se envia mail y muestra mensaje en pantalla
#Si es igual a 200, Sample-App funciona y se muestra mensaje en pantalla
try:
	r = requests.head(sitio)

	if r.status_code != 200:
		print "SAMPLE-APP ESTA CAIDA! ENVIANDO ALERTA POR EMAIL"
		send_mail()
	else :
		print "Sample-App esta funcionando y devuelve el codigo: " + str(r.status_code)
except:
	print "SAMPLE-APP ESTA CAIDA! ENVIANDO ALERTA POR EMAIL"
	send_mail()
