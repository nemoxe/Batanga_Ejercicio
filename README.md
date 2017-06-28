# Prueba Devops Batanga

Para la primer parte de la prueba, se encuentra el script "test_query.py"

Para la segunda prueba:

Al ejecutar "vagrant up" se crean los 3 equipos pedidos en el ejericio con la aplicacion Sample-App funcionando.
Se forwardea el puerto 3000 del equipo guest al puerto 80 de la vm nginx.devops.com para que se pueda ver que
sample-app esta funcionando, para esto ingresamos a http://127.0.0.1:3000

El provisioning de las vms se realiza mediante Puppet, los modulos para cada paquete estan en "provision/modules"
y la declaracion de nodos en "provision/manifests/default.pp"
Para notificar via mail que Sample-App ha dejado de estar en estado de produccion
se encuentra el script "test_sample_app.py"
